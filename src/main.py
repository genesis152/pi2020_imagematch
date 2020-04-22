import cv2
import numpy as np
from defs import *
from metrics import *


def testMetrics():
    keypointA = Keypoint([0, 0],
                         [120, 120, 120],
                         [0, 3, 1])
    keypointB = Keypoint([50, 50],
                         [120, 120, 120],
                         [0, 3, 1])
    print("Identical points")
    print("Euclidian distance : ", distance(keypointA, keypointB))
    print("Cosine distance : ", cosineSimilarity(keypointA, keypointB))
    keypointA = Keypoint([0, 0],
                         [120, 120, 120],
                         [0, 3, 1])
    keypointB = Keypoint([50, 50],
                         [255, 255, 255],
                         [1201020, 1201020, 1])
    print("Very different point")
    print("Euclidian distance : ", distance(keypointA, keypointB))
    print("Cosine distance : ", cosineSimilarity(keypointA, keypointB))


if __name__ == "__main__":
    testMetrics()
    print("Hello!")
    img = np.zeros((128, 128, 3), dtype=np.uint8)
    img[:, :, 1] = 128
    cv2.imshow("img", img)
    cv2.waitKey()
