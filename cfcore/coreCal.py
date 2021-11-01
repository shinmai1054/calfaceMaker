# カレンダー計算モジュール
# cfcore/coreCal.py

import calendar


def getLabel(firstweekday=calendar.SUNDAY):
    if not 0 <= firstweekday <= 6:
        firstweekday=calendar.SUNDAY

    label = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return label[firstweekday:7] + label[0:firstweekday]


def calcCalendar(y, m, firstweekday=calendar.SUNDAY):
    c = calendar.Calendar()
    c.firstweekday = firstweekday
    cal = c.monthdayscalendar(y, m)
    return cal


if __name__ == '__main__':
    print(getLabel(0))
    print(calcCalendar(2021, 11, 0))
