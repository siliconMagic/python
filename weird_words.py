#! /usr/bin/python


def to_weird_case(string):
	weird_words =[]
	for word in string.split():
		weird = ''
		for i, letter in enumerate(word):
			if i % 2 == 0:
				weird += letter.upper()
			else:
				weird += letter.lower()
		weird_words.append(weird)
	return ' '.join(weird_words)

print(to_weird_case('This is a test.'))

