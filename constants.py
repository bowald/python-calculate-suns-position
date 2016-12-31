# Tables comes from http://aa.quae.nl/en/reken/zonpositie.html
# Wich cites International Astronomical Union(IAU) 2011

# Table 1: Planets: Mean anomaly
# value 0 is in degressas and value 1 is in degress per day
planetToMeanAnomaly = {
    'Mercury': (174.7948, 4.09233445),
    'Venus': (50.4161, 1.60213034),
    'Earth': (357.5291, 0.98560028),
    'Mars': (19.3730, 0.52402068),
    'Jupiter': (20.0202, 0.08308529),
    'Saturn': (317.0207, 0.03344414),
    'Uranus': (141.0498, 0.01172834),
    'Neptune': (256.2250, 0.00598103),
    'Pluto': (14.882, 0.00396)
}

# Table 2: Planets: Equation of Center
# Each planets coefficients, the more coefficients needed
# the more it devieates from a perfect sphere
planetToCenterCoefficients = {
    'Mercury': [23.4400, 2.9818, 0.5255, 0.1058, 0.0241, 0.0055],
    'Venus': [0.7758, 0.0033],
    'Earth': [1.9148, 0.0200, 0.0003],
    'Mars': [10.6912, 0.6228, 0.0503, 0.0046, 0.0005],
    'Jupiter': [5.5549, 0.1683, 0.0071, 0.0003],
    'Saturn': [6.3585, 0.2204, 0.0106, 0.0006],
    'Uranus': [5.3042, 0.1534, 0.0062, 0.0003],
    'Neptune': [1.0302, 0.0058],
    'Pluto': [28.3150, 4.3408, 0.9214, 0.2235, 0.0627]
}

# Table 3: Planets: Perihelion and Obliquity of the Ecliptic (Planetocentric)
# Perihelion = closest point to the sun on a planet orbiting the sun.
planetToPeriheion = {
    'Mercury': 230.3265,
    'Venus': 73.7576,
    'Earth': 102.9373,
    'Mars': 71.0041,
    'Jupiter': 237.1015,
    'Saturn': 99.4587,
    'Uranus': 5.4634,
    'Neptune': 182.2100,
    'Pluto': 184.5484
}

# Obliquity = axial tilt
planetToObliquity = {
    'Mercury': 0.0351,
    'Venus': 2.6376,
    'Earth': 23.4393,
    'Mars': 25.1918,
    'Jupiter': 3.1189,
    'Saturn': 26.7285,
    'Uranus': 82.2298,
    'Neptune': 27.8477,
    'Pluto': 119.6075
}

# Table $: Planets: Approximations for Right Ascension and Declination
planetToAscension = {
    'Mercury': [0.0],
    'Venus': [-0.0304],
    'Earth': [-2.4657, 0.0529, -0.0014],
    'Mars': [2.8608, 0.0713, -0.0022],
    'Jupiter': [-0.0425],
    'Saturn': [-3.2338, 0.0909, -0.0031],
    'Uranus': [-42.5874, 12.8117, -2.6077],
    'Neptune': [-3.5214, 0.1078, -0.0039],
    'Pluto': [-19.3248, 3.0286, -0.4092]
}

planetToDeclination = {
    'Mercury': [0.0351],
    'Venus': [2.6367, 0.0009],
    'Earth': [22.7908, 0.5991, 0.0492],
    'Mars': [24.3880, 0.7332, 0.0706],
    'Jupiter': [3.1173, 0.0015],
    'Saturn': [25.7696, 0.8640, 0.0949],
    'Uranus': [56.9083, -0.8433, 26.1648],
    'Neptune': [26.7643, 0.9669, 0.1166],
    'Pluto': [49.8309, 4.9707, 5.5910]
}

# Table 5: Planets: Sidereal Time
# Coefficiants used to calculate sidereal time
planetToSiderealTimeCoefficients = {
    'Mercury': (132.3282, 6.1385025),
    'Venus': (104.9067, -1.4813688),
    'Earth': (280.1470, 360.9856235),
    'Mars': (313.3827, 350.89198226),
    'Jupiter': (145.9722, 870.5360000),
    'Saturn': (174.3508, 810.7939024),
    'Uranus': (29.6474, -501.1600928),
    'Neptune': (52.4160, 536.3128662),
    'Pluto': (122.2370, 56.3625225)
}

# Table 6: Planets: Noon
planetToNoon = {
    'Mercury': [45.3497, 11.4556, 0.0, 175.9386],
    'Venus': [52.1268, -0.2516, 0.0099,  -116.7505],
    'Earth': [0.0009, 0.0053, -0.0068, 1.0000000],
    'Mars': [0.9047, 0.0305, -0.0082, 1.027491],
    'Jupiter': [0.3345, 0.0064, 0.0, 0.4135778],
    'Saturn': [0.0766, 0.0078, -0.0040, 0.4440276],
    'Uranus': [0.1260, -0.0106, 0.0850, -0.7183165],
    'Neptune': [0.3841, 0.0019, -0.0066, 0.6712575],
    'Pluto': [4.5635, -0.5024, 0.3429, 6.387672]
}

# Table 7: Planets: Contributions to the Equation of Time
planetToOrbitContribution = {
    'Mercury': 94.5,
    'Venus': 3.1,
    'Earth': 7.7,
    'Mars': 42.8,
    'Jupiter': 22.2,
    'Saturn': 25.4,
    'Uranus': 21.2,
    'Neptune': 4.1,
    'Pluto': 114.6
}

planetToSesonalContribution = {
    'Mercury': 0,
    'Venus': 0.1,
    'Earth': 9.9,
    'Mars': 11.4,
    'Jupiter': 0.2,
    'Saturn': 13.0,
    'Uranus': 178.1,
    'Neptune': 14.1,
    'Pluto': 69.3
}

# Table 8: Planets: Daytime Length Coefficients
planetToDaytimeLengthCoefficients = {
    'Mercury': [0.035],
    'Venus': [2.636, 0.001, ],
    'Earth': [22.137, 0.599, 0.016],
    'Mars': [23.576, 0.733, 0.024],
    'Jupiter': [3.116, 0.00],
    'Saturn': [24.800, 0.864, 0.032],
    'Uranus': [28.680, -0.843, 8.722],
    'Neptune': [26.668, 0.967, 0.039],
    'Pluto': [38.648, 4.971, 1.864]
}

# Table 9: Planets: Solar Disk Diameter and Refraction
# Sunrise and sunset needs to account for two facts:
# 1: sun is seen as a disc, meaning that when the sun sets,
#    half of the disc is still visiable.
planetToSunDiskDiameter = {
    'Mercury': 1.38,
    'Venus': 0.74,
    'Earth': 0.53,
    'Mars': 0.35,
    'Jupiter': 0.10,
    'Saturn': 0.06,
    'Uranus': 0.03,
    'Neptune': 0.02,
    'Pluto': 0.01
}

# 2: The atmosphere bends the light downwards,
#    making the sun look higher in the sky than it actually is
planetToAtmosphericRefraction = {
    'Mercury': -0.69,
    'Venus': -0.37,
    'Earth': -0.83,
    'Mars': -0.17,
    'Jupiter': -0.05,
    'Saturn': -0.03,
    'Uranus': -0.01,
    'Neptune': -0.01,
    'Pluto': -0.01
}
