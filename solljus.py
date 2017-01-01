import math
import datetime
import pytz
import constants as c


# Sin with degrees as input
def sin(deg):
    return math.sin(math.radians(deg))


# Cos with degrees as input
def cos(deg):
    return math.cos(math.radians(deg))


# Tan with degrees as input
def tan(deg):
    return math.tan(math.radians(deg))


# Arcsin with  degrees as input
def asin(x):
    return math.degrees(math.asin(x))


def acos(x):
    return math.degrees(math.acos(x))


def atan(x):
    return math.degrees(math.atan(x))


# Julian date based on algorithm from
# https://en.wikipedia.org/wiki/Julian_day
def getJulianDateFromDateTime(date):
    a = (14 - date.month)/12
    y = date.year + 4800 - a
    m = date.month + 12 * a - 3

    terms = [0] * 10
    terms[0] = date.day
    terms[1] = (153 * m + 2) / 5
    terms[2] = 365 * y
    terms[3] = y / 4
    terms[4] = -(y / 100)
    terms[5] = y / 400
    terms[6] = -32045
    terms[7] = float(date.time().hour - 12) / 24.0
    terms[8] = float(date.time().minute) / 1440.0
    terms[9] = float(date.time().second) / 86400.0
    return sum(terms)


def getPlanetMeanAnomaly(julianDate, planet='Earth'):
    degrees, degreesPerDay = c.planetToMeanAnomaly[planet]
    return (degrees + degreesPerDay * (math.floor(julianDate) - c.j2000)) % 360


def getCenter(mean, planet='Earth'):
    CTerms = c.planetToCenterCoefficients[planet]
    return sum([t * sin(i * mean) for i, t in enumerate(CTerms, 1)])


def getEclipticalCoordinates(meanAnomaly, center, planet='Earth'):
    E = c.planetToPeriheion[planet]
    nu = meanAnomaly + center
    olambda = nu + E
    sunLambda = olambda + 180.0
    return sunLambda % 360.0


def getEquatorialCoordinates(sunLambda, planet='Earth'):
    A = c.planetToAscension[planet]
    D = c.planetToDeclination[planet]
    alfa = sunLambda + sum([a * sin(i * 2 * sunLambda) for i, a in enumerate(A, 1)])
    delta = sum([D[i] * pow(sin(sunLambda), i * 2 + 1) for i in range(len(D))])
    return alfa, delta


def getAzimutandAltitude(julianDate,
                         alfa,
                         delta,
                         longitude,
                         latitude,
                         planet='Earth'):

    theta0, theta1 = c.planetToSiderealTimeCoefficients[planet]
    # Longitude should be given as east(if it given in degrees west, negate it)
    siderealTime = (theta0 + theta1 * (julianDate - c.j2000) + longitude) % 360
    H = siderealTime - alfa

    a0 = sin(H)
    a1 = cos(H) * sin(latitude) - tan(delta) * cos(latitude)
    A = atan(a0 / a1)

    h = asin(sin(latitude) * sin(delta) + cos(latitude) * cos(delta) * cos(H))
    print 'h', h
    return A, h


# Implementation is based on
# http://aa.quae.nl/en/reken/zonpositie.html
def calculatePositionOfTheSun(planet='Earth',
                              longitude=57.711338,
                              latitude=12.022330):

    debugExample = datetime.datetime(2004, 04, 1, 12, 00, 00, 00, tzinfo=pytz.utc)
    debugLongitude = 5.0
    debugLatitude = 52.0
    # 1 time
    now = datetime.datetime.utcnow()
    julianDate = getJulianDateFromDateTime(debugExample)

    # 2 The mean anomaly
    meanAnomaly = getPlanetMeanAnomaly(julianDate, planet)

    # 3 The equation of center
    center = getCenter(meanAnomaly, planet)

    # 5 The Ecliptical Coordinates
    sunLambda = getEclipticalCoordinates(meanAnomaly, center, planet)

    # 6 The Equatorial coordinates
    alfa, delta = getEquatorialCoordinates(sunLambda, planet)

    # 7 The Observer
    # Sidereal time is the right ascension(think longitude for the sky)
    # that is on the celestial meridian at that moment.
    # Hour angle indicates gow long ago(measured in sidereal time)
    # the celestial body passed through the celestial meridian
    sunAzimuth, sunAltitude = getAzimutandAltitude(julianDate,
                                                   alfa,
                                                   delta,
                                                   debugLongitude,
                                                   debugLatitude,
                                                   planet)

if __name__ == '__main__':
    calculatePositionOfTheSun()
