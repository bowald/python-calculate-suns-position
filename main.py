import math
import datetime

LONGITUDE = 57.711338
LATITUDE = 12.022330


def sin(deg):
    return math.sin(math.radians(deg))


def getCurrentJulianDate():
    now = datetime.datetime.utcnow()
    return getJulianDateFromDateTime(now)


# Julian date based on algorithm from
# https://en.wikipedia.org/wiki/Julian_day
def getJulianDateFromDateTime(date):
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
    terms[6] = float(date.time().hour - 12) / 24.0
    terms[7] = float(date.time().minute) / 1440.0
    terms[8] = float(date.time().second) / 86400.0
    return sum(terms)


def getEarthMeanAnonmaly(julianDate):
    EarthDeg = 357.5291
    EarthDegPerDay = 0.98560028
    return getPlanetMeanAnomaly(EarthDeg, EarthDegPerDay, julianDate)


def getPlanetMeanAnomaly(degrees, degreesPerDay, julianDate):
    j2000 = 2451545
    return (degrees + degreesPerDay * (julianDate - j2000)) % 360


def getCenterForEarth(mean):
    CTerms = [1.9148, 0.02, 0.0003]
    return getCenter(CTerms, mean)


def getCenter(CTerms, mean):
    return sum([t * sin(i * mean) for i, t in enumerate(CTerms, 1)])


# Implementation is based on
# http://aa.quae.nl/en/reken/zonpositie.html
def main():
    # 1 time
    julianDate = getCurrentJulianDate()
    # 2 The mean anomaly
    meanAnomaly = getEarthMeanAnonmaly(julianDate)
    # 3 The equation of center
    # True anomaly = Mean Anomaly + center
    center = getCenterForEarth(meanAnomaly)
    print center


if __name__ == '__main__':
    main()
