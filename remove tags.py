def remove_tags(s):
    text_list = []
    text = []
    if '<' not in s:
        return s.split()
    while s:
    	if s[0] == '<':
    		s = s[s.find('>')+1:]
    	else:
    		if '<' not in s:
    			text = s.split()
    			text_list = text_list + text
    			return text_list
    		else:
    			text = s[:s.find('<')].split()
    			text_list = text_list + text
    			s = s[s.find('>')+1:]
    return text_list




s1 = '''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>'''

print remove_tags(s1)

s2 = '''<table cellpadding='3'>
                      <tr><td>Hello</td><td>World!</td></tr>
                      </table>'''

print remove_tags(s2)

s3 = "<hello><goodbye>"

print remove_tags(s3)

s4 = "This is plain text."

print remove_tags(s4)

s5 = "<br />This line starts with a tag"

print remove_tags(s5)