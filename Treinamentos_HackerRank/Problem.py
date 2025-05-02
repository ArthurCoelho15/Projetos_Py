"""

HackerRank: https://www.hackerrank.com/challenges/robot/problem?isFullScreen=true



"""


def is_leap(year):
    if year % 4 == 0:
        if year % 100 and year % 400:
            return True
        else:
            return True
    return False


year = int(input())
print(is_leap(year))