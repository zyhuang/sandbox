'''A module for demonstrating exceptions.'''

from math import log

def convert(s):
    '''Convert to an integer.'''

    x = -1
    try:
        x = int(s)

    except (ValueError, TypeError) as e:

        print('Conversion failed due to: {}'.format(str(e)))
        raise

    return x



def string_log(s):

    v = convert(s)
    return log(v)



# print(convert('a'))
# print(convert([1,2,3]))
# print(string_log("ouch"))
print(string_log([1,2,3]))
