import re

regex = r'.([\d]+).([A]+).([$]+).|' \
        r'.([\d]+).([$]+).([A]+).|' \
        r'.([$]+).([\d]+).([A]+).|' \
        r'.([$]+).([A]+).([\d]+).|' \
        r'.([A]+).([\d]+).([$]+).|' \
        r'.([A]+).([$]+).([\d]+).|'

pat = re.compile(regex)

myStr = "hk5hA$"


def check(pattern='', string=''):
    if re.fullmatch(pattern=pattern, string=string):
        return True
    else:
        return False


print(check(pattern=pat, string=myStr))
