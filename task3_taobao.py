"""
实现登录淘宝网站，并输入搜索关键词查找商品，然后完成商品信息爬取，存储数据库
数据库使用MONGO DB
"""
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from pyquery import PyQuery as PQ

from dbConfig import *
import pymongo

"""
配置数据库信息
"""
client = pymongo.MongoClient(MONGO_CONN)
db = client[MONGO_DB]

# options = webdriver.FirefoxOptions()
# options.add_argument('disable-blink-features=AutomationControlled')
browser = webdriver.Firefox()

def test_login():
    # 淘宝登录
    browser.get('https://www.taobao.com') # 刚才网站输入错误
    # 等待页面加载，需要搜索按钮出现即可，等到时间设置为10秒钟
    e_search = WDW(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))

    # 点击搜索按钮: 出现登录框
    e_search.click()

    # 如果初次登录，则在登录框中用手机扫码登录，并将cookie保存到本地，下次直接读取cookie登录
    time.sleep(30) # 留给扫码的时间


    # 获取cookies
    log_cookies = browser.get_cookies()

    # cookies保存到本地
    with open('cookies/taobao_log_cookies', 'w') as f:
        f.write(json.dumps(log_cookies))
        print('TaoBao cookies have been saved successfully')

    browser.close()

def search():
    # 登录并搜索
    browser.get('https://taobao.com')
    with open('cookies/taobao_log_cookies', 'r') as f:
        log_cookies = json.loads(f.read())
        # 加载cookies
        for cookie in log_cookies:
            dict_cookies = {
                'domain': '.taobao.com',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                'path': '/',
                'expires': '',
                'sameSite': 'None',
                'secure': cookie.get('secure')
            }

            browser.add_cookie(dict_cookies) # 这里注意缩进

    try:
        browser.get('https://taobao.com') # 这里需要再登录一下
        # 找到搜索框
        e_input = WDW(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )

        # 找到提交按钮
        e_submit = WDW(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-search'))
        )

        # 加入停顿
        time.sleep(2)
        e_input.send_keys('GPU')
        time.sleep(2)
        e_submit.click()

        # 当下一页按钮出现时，返回页面内容
        tot_page = WDW(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.next-btn:nth-child(11)'))
        )
        return tot_page.text

    except TimeoutError:
        print('Time Out')
        return search()


# 翻页逻辑
def next_page(page_number):
    # 定位下一页输入栏
    e_input = WDW(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span.next-input:nth-child(6) > input:nth-child(1)'))
    )

    # 下一页确定按钮
    e_submit = WDW(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.next-pagination-jump-go'))
    )

    time.sleep(2)
    e_input.clear()
    e_input.send_keys(page_number)
    e_submit.click()


# 获取商品详细信息
def get_product():
    WDW(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'li.next-tabs-tab:nth-child(1) > div:nth-child(1)'))
    )

    time.sleep(2)

    html = browser.page_source # 获取网页源代码
    doc = PQ(html)
    items = doc('div[class^="Card--doubleCard"]').items()

    for item in items:
        product = {
            'name': item.find('div[class^="Title--title"] span').text(),
            'image': item.find('img').attr('src'),
            'price': item.find('div[class^="Price--priceWrapper"] span[class^="Price--priceInt"]').text() + item.find(
                'div[class^="Price--priceWrapper"] span[class^="Price--priceFloat"]').text(),
            'deal': item.find('div[class^="Price--priceWrapper"] span[class^="Price--realSales"]').text()[:-3],
            'source': item.find('span[class^="Price--procity"]').text()
        }
        print(product) # 输出商品详情
        save_in_mongo(product)


# 数据保存到MongoDB数据库中：数据库配置文件 dbConfig.py
def save_in_mongo(res):
    try:
        if db[MONGO_TABLE].insert_one(res):
            print('Insert to Mongo DB successfully')
    except Exception as err:
        print('Store Error')
        print(err)


def main():
    tot_page = int(search())
    if tot_page >=2:
        for i in range(1, min(tot_page, 11)):
            print('Get page: ', i)
            get_product()
            next_page(i)

    browser.close()


if __name__ == '__main__':
    main()