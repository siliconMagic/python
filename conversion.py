# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. Itcan
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and
#     a string, and returns the result of applying the converter to the
#     input string. This replaces all occurrences of the match used to
#     build the converter, with the replacement.  It keeps doing
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):

    '''
    docstring
    '''

    code = []
    code.append(match)
    code.append(replacement)
    return code


def apply_converter(converter, string):

    '''
    docstring
    '''

    while converter[0] in string:
        string = string.replace(converter[0], converter[1], 1)
    return string


# For example,
TEST1 = make_converter('aa', 'a')
print(apply_converter(TEST1, 'aaaa'))
# >>> a

TEST2 = make_converter('aba', 'b')
print(apply_converter(TEST2, 'aaaaaabaaaaa'))
# >>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would
# run forever).
