import math
import datetime
import constants as c


# Sin with degrees as input
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


def getPlanetMeanAnomaly(julianDate, planet='Earth'):
    degrees, degreesPerDay = c.planetToMeanAnomaly[planet]
    j2000 = 2451545
    return (degrees + degreesPerDay * (math.floor(julianDate) - j2000)) % 360


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


# Implementation is based on
# http://aa.quae.nl/en/reken/zonpositie.html
def calculatePositionOfTheSun(planet='Earth'):
    # 1 time
    julianDate = getCurrentJulianDate()

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
    # siderealTime, hourAngle = getSiderealTimeAndHourAngle(julianDate,
    #                                                            LONGITUDE,
    #                                                            LATITUDE)

if __name__ == '__main__':
    calculatePositionOfTheSun()
