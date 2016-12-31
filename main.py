import math
import datetime
import constants as c


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


def getEclipticalCoordinatesRelativeToEarth(meanAnomaly, center, E):
    nu = meanAnomaly + center
    olambda = nu + E
    lambdaSun = olambda + 180.0
    return lambdaSun % 360.0


def getEarthEquatorialCoordinates(sunLambda):
    A = [-2.4657, 0.0529, -0.0014]
    Ea = 0.0003
    D = [22.7908, 0.5991, 0.0492]
    Ed = 0.0003
    return getEquatorialCoordinates(A, D, sunLambda)


def getEquatorialCoordinates(A, D, sunLambda):
    alfa = sunLambda + sum([a * sin(i * 2 * sunLambda) for i, a in enumerate(A, 1)])
    delta = sum([D[i] * pow(sin(sunLambda), i * 2 + 1) for i in range(len(D))])
    return alfa, delta


# Implementation is based on
# http://aa.quae.nl/en/reken/zonpositie.html
def main():
    # 1 time
    julianDate = getCurrentJulianDate()

    # 2 The mean anomaly
    meanAnomaly = getEarthMeanAnonmaly(julianDate)

    # 3 The equation of center
    center = getCenterForEarth(meanAnomaly)

    # 4 The Perihelion and the Obliquity of the Ecliptic
    E, e = getEarthEclipticLongitude()

    # 5 The Ecliptical Coordinates
    sunLambda = getEclipticalCoordinatesRelativeToEarth(meanAnomaly,
                                                        center,
                                                        E)
    # 6 The Equatorial coordinates
    alfa, delta = getEarthEquatorialCoordinates(sunLambda)

    # 7 The Observer
    # Sidereal time is the right ascension(think longitude for the sky) that is on the
    # celestial meridian at that moment.
    # Hour angle indicates gow long ago(measured in sidereal time)
    # the celestial body passed through the celestial meridian
    # siderealTime, hourAngle = getSiderealTimeAndHourAngle(julianDate,
    #                                                            LONGITUDE,
    #                                                            LATITUDE)



if __name__ == '__main__':
    main()
