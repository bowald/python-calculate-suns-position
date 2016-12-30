import math
import datetime

LONGITUDE = 57.711338
LATITUDE = 12.022330


def sin(deg):
    return math.sin(math.radians(deg))


def getCurrentJulianDate():
    now = datetime.datetime.now()
    return getJulianDateFromDateTime(now)


# Julian date based on algorithm from
# https://en.wikipedia.org/wiki/Julian_day
def getJulianDateFromDateTime(date):
    a = int((14 - date.month)/12)
    y = date.year + 4800 - a
    m = date.month + 12 * a - 3

    terms = [0] * 10
    terms[0] = date.day
    terms[1] = (153 * m + 2) / 5
    terms[2] = 365 * y
    terms[3] = y / 4
    terms[4] = -y / 100
    terms[5] = y / 400
    terms[6] = -32045
    terms[7] = float(date.time().hour - 12) / 24.0
    terms[8] = float(date.time().minute) / 1440.0
    terms[9] = float(date.time().second) / 86400.0
    return sum(terms)


def getEarthMeanAnonmaly(julianDate):
    EarthDeg = 357.5291
    EarthDegPerDay = 0.98560028
    return getPlanetMeanAnomaly(EarthDeg, EarthDegPerDay, julianDate)


def getPlanetMeanAnomaly(degrees, degreesPerDay, julianDate):
    j2000 = 2451545
    return (degrees + degreesPerDay * (math.floor(julianDate) - j2000)) % 360


def getCenterForEarth(mean):
    CTerms = [1.9148, 0.02, 0.0003]
    return getCenter(CTerms, mean)


def getCenter(CTerms, mean):
    return sum([t * sin(i * mean) for i, t in enumerate(CTerms, 1)])

# The ecliptic longitude of Earth as seen from the Sun
def getEarthEclipticLongitude():
    return 102.9373, 23.4393


def getEclipticalCoordinatesRelativeToEarth(meanAnomaly, center, E, e):
    nu = meanAnomaly + center
    olambda = nu + E
    lambdaSun = olambda + 180.0
    return lambdaSun % 360.0
# Implementation is based on
# http://aa.quae.nl/en/reken/zonpositie.html
def main():
    # 1 time
    julianDate = getCurrentJulianDate()
    print julianDate
    # 2 The mean anomaly
    meanAnomaly = getEarthMeanAnonmaly(julianDate)
    #meanAnomaly = 87.1807
    # 3 The equation of center
    # True anomaly = Mean Anomaly + center
    center = getCenterForEarth(meanAnomaly)

    E, e = getEarthEclipticLongitude()
    sunLambda = getEclipticalCoordinatesRelativeToEarth(meanAnomaly, center, E, e)
    print sunLambda

if __name__ == '__main__':
    main()
