# from segmentation import *
# from coding import *


# def compare_codes(a, b, mask_a, mask_b, rotation=False):
#     if rotation:
#         d = []
#         for i in range(-rotation, rotation + 1):
#             c = np.roll(b, i, axis=1)
#             mask_c = np.roll(mask_b, i, axis=1)
#             d.append(np.sum(np.remainder(a + c, 2) * mask_a * mask_c) / np.sum(mask_a * mask_c))
#         return np.min(d)
#     return np.sum(np.remainder(a + b, 2) * mask_a * mask_b) / np.sum(mask_a * mask_b)

# def encode_photo(image):

#     img = preprocess(image)
#     x, y, r = find_pupil_hough(img)
#     x_iris, y_iris, r_iris = find_iris_hough(img)
#     iris = unravel_iris(image, x, y, r, x_iris, y_iris, r_iris)
#     return iris_encode(iris)

# if __name__ == '__main__':
#     image = cv2.imread('splash-eye.jpg')
#     image2 = cv2.imread('splash-eye.jpg')
#     print(image.shape)
#     print(image2.shape)
#     code, mask = encode_photo(image)
#     code2, mask2 = encode_photo(image2)

#     if compare_codes(code, code2, mask, mask2) == 0:
#         print(compare_codes(code, code2, mask, mask2))
#         print("Iris Matched")
#     else:
#         print("No match found")
#         print("Difference: "+str(compare_codes(code, code2, mask, mask2)))


import argparse
import cv2
from segmentation import *
from coding import *

def compare_codes(a, b, mask_a, mask_b, rotation=False):
    if rotation:
        d = []
        for i in range(-rotation, rotation + 1):
            c = np.roll(b, i, axis=1)
            mask_c = np.roll(mask_b, i, axis=1)
            d.append(np.sum(np.remainder(a + c, 2) * mask_a * mask_c) / np.sum(mask_a * mask_c))
        return np.min(d)
    return np.sum(np.remainder(a + b, 2) * mask_a * mask_b) / np.sum(mask_a * mask_b)

def encode_photo(image):
    img = preprocess(image)
    x, y, r = find_pupil_hough(img)
    x_iris, y_iris, r_iris = find_iris_hough(img)
    iris = unravel_iris(image, x, y, r, x_iris, y_iris, r_iris)
    return iris_encode(iris)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compare iris codes from two images.")
    parser.add_argument("image1", type=str, help="Path to the first image")
    parser.add_argument("image2", type=str, help="Path to the second image")
    args = parser.parse_args()

    # Load the images
    image1 = cv2.imread(args.image1)
    image2 = cv2.imread(args.image2)

    if image1 is None or image2 is None:
        print("Error: One or both images could not be loaded. Check file paths.")
        exit(1)

    print(f"Image 1 shape: {image1.shape}")
    print(f"Image 2 shape: {image2.shape}")

    # Encode the iris codes
    code1, mask1 = encode_photo(image1)
    code2, mask2 = encode_photo(image2)

    # Compare the codes
    if compare_codes(code1, code2, mask1, mask2) == 0:
        print("Iris Matched")
    else:
        diff = compare_codes(code1, code2, mask1, mask2)
        print("No match found")
        print(f"Difference: {diff}")
