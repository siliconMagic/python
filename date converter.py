def date_converter(d, s):
    month = s[:s.find('/')]
    month = d[int(month)]
    day = s[s.find('/')+1:]
    day = day[:day.find('/')]
    year = s[s.find('/')+1:]
    year = year[year.find('/')+1:]
    return day +' '+ month +' '+ year
    




english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}


print date_converter(english, '11/3/1848')
#>>> 11 May 2012

print date_converter(english, '5/11/12')
#>>> 11 May 12

print date_converter(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter(swedish, '12/5/1791')
#>>> 5 december 1791