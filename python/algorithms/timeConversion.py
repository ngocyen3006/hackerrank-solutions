# https://www.hackerrank.com/challenges/time-conversion/problem

import re


def timeConversion(s):
    if re.match("^12(.)+AM$", s):
        res = '00' + s[2:8]
        return res

    if re.match("^(.)+AM$|^12(.)+PM$", s):
        return s[:8]

    res = int(s[:2]) + 12
    return str(res) + s[2:8]
