import math
import datetime

LONGITUDE = 57.711338
LATITUDE = 12.022330


def getCurrentJulianDate():
    now = datetime.datetime.utcnow()
    return getJulianDateFromTime(now)


# Julian date based on algorithm from
# https://en.wikipedia.org/wiki/Julian_day
def getJulianDateFromTime(date):
    a = int((14 - date.month)/12)
    y = date.year + 4800 - a
    m = date.month + 12 * a - 3

    terms = [0] * 9
    terms[0] = (153 * m + 2) / 5
    terms[1] = 365 * y
    terms[2] = y / 4
    terms[3] = -y / 100
    terms[4] = y / 400
    terms[5] = -32045
    terms[6] = float(date.time().hour - 12) / float(24)
    terms[7] = float(date.time().minute) / float(1440)
    terms[8] = float(date.time().second) / float(86400)
    return sum(terms)


# Implementation is based on
# http://aa.quae.nl/en/reken/zonpositie.html

def main():
    jd = getCurrentJulianDate()
    print jd

if __name__ == '__main__':
    main()
