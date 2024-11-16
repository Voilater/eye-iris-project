import matplotlib.pyplot as plt
import cv2
import numpy as np


def show_segment(img, x, y, r, x2=None, y2=None, r2=None):
    ax = plt.subplot()
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    segment = plt.Circle((x, y), r, color='b', fill=False)
    ax.add_artist(segment)
    if r2 is not None:
        segment2 = plt.Circle((x2, y2), r2, color='r', fill=False)
        ax.add_artist(segment2)
    plt.show()

def preprocess(image):
    img = image[:, :, 0].copy()
    img[img > 225] = 30
    return cv2.medianBlur(img, 21)


def find_pupil_hough(img):
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=10, maxRadius=200)
    circles = np.uint16(np.around(circles))
    return circles[0, 0][0], circles[0, 0][1], circles[0, 0][2]

def find_iris_hough(img):

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=10, maxRadius=200)
    circles = np.uint16(np.around(circles))
    return circles[0, 0][0], circles[0, 0][1], circles[0, 0][2]

if __name__ == '__main__':
    image = cv2.imread("iris1.bmp")
    newImage = image.copy()
    img = preprocess(image)
    img1 = preprocess(newImage)
    x, y, r = find_pupil_hough(img)
    x_iris, y_iris, r_iris = find_iris_hough(img1)
    # show_segment(image, x, y, r, x_iris, y_iris, r_iris)
