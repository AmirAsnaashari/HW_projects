import datetime
import calendar


def find_day(entry):
    day = datetime.datetime.strptime(entry, '(%d, %m, %Y)').weekday()
    return calendar.day_name[day]


def find_month(entry):
    month = datetime.datetime.strptime(entry, '(%d, %m, %Y)').month
    return calendar.month_name[month]


entry = '(03, 04, 1998)'
print(find_day(entry), find_month(entry), '1998')
