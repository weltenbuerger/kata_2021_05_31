# https://www.codewars.com/kata/517abf86da9663f1d2000003
import re


def to_camel_case(text):
    words = re.split('_|-', text)
    camelized = ''
    for idx, word in enumerate(words):
        if idx is 0:
            camelized += word
        else:
            camelized += word.capitalize()
    return camelized


# alternative:


def to_camel_case2(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s


print(to_camel_case('A-pippi_Is-Omoshiroi'))
