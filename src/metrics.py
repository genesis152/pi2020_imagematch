from defs import *
from numpy import sqrt


# the distance is computed based on color and direction
# metric computed as weighted average
def distance(keypointA, keypointB):
    colorWeight = 1
    directionWeight = 1

    assert (isinstance(keypointA, Keypoint))
    assert (isinstance(keypointB, Keypoint))

    colorMetric = sqrt(((keypointA.color[0] - keypointB.color[0]) ** 2) +
                       ((keypointA.color[1] - keypointB.color[1]) ** 2) +
                       ((keypointA.color[2] - keypointB.color[2]) ** 2))

    dimension = len(keypointA.direction)
    directionMetric = 0
    for i in range(dimension):
        directionMetric += (keypointA.direction[i] - keypointB.direction[i]) ** 2
    directionMetric = sqrt(directionMetric)

    return (directionWeight * directionMetric + colorWeight * colorMetric) / (colorWeight + directionWeight)


def cosineSimilarity(keypointA, keypointB):
    assert (isinstance(keypointA, Keypoint))
    assert (isinstance(keypointB, Keypoint))

    numerator = (keypointA.color[0] * keypointB.color[0] +
                 keypointA.color[1] * keypointB.color[1] +
                 keypointA.color[2] * keypointB.color[2])
    dimension = len(keypointA.direction)
    for i in range(dimension):
        numerator += keypointA.direction[i] * keypointB.direction[i]

    dimension = len(keypointA.color)
    denominatorA = 0
    denominatorB = 0
    for i in range(dimension):
        denominatorA += keypointA.color[i] ** 2
        denominatorB += keypointB.color[i] ** 2
    dimension = len(keypointA.direction)
    for i in range(dimension):
        denominatorA += keypointA.direction[i] ** 2
        denominatorB += keypointB.direction[i] ** 2

    return numerator / (sqrt(denominatorA) * sqrt(denominatorB))
