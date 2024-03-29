import requests
from requests.exceptions import RequestException
import re
import json
import os
from multiprocessing import Pool

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # print(response.encoding) 查看网页编码格式
            response.encoding = 'UTF-8'  # 改变编码格式
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?><a.*?>(.*?)</a>.*?<p class="star">(.*?)</p>.*?>('
        '.*?)</p>.*?<i class="integer">(.*?)</i>.*?fraction">(.*?)</i>',
        re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('ou-files/maoyan.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://www.maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    if os.path.exists('ou-files/maoyan.txt'):
        os.remove('ou-files/maoyan.txt')
    elif not os.path.exists('ou-files'):
        os.mkdir('ou-files')

    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
