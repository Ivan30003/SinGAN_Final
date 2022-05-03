from argparse import ArgumentParser

import cv2 as cv
import argparse


def test_result_image():
    # parser: ArgumentParser = argparse.ArgumentParser(description='comparison of two images')
    # parser.add_argument('--result-image-path', default='results/result_image/s9/s0_sampled.png', help='')
    # parser.add_argument('--checking-image-path', default='results/images_for_verifying/s9/s0_sampled.png', help='path'
    #                     'for checking image. Test will be OK if your first result image is equal or almost equal to '
    #                     'first checking image')
    # args = parser.parse_args()

    image_1 = cv.imread('results/result_images/s9/s0_sampled.png')
    image_2 = cv.imread('results/images_for_verifying/s9/s0_sampled.png')

    images_1_components = image_1[:, :, 0], image_1[:, :, 1], image_1[:, :, 2]
    images_2_components = image_2[:, :, 0], image_2[:, :, 1], image_2[:, :, 2]

    test_verdict = True
    for i in range(0, 3):
        for j in range(len(images_1_components[0])):
            for k in range(len(images_1_components[0][0])):
                if images_1_components[i][j][k] > images_2_components[i][j][k]:
                    if images_1_components[i][j][k] - images_2_components[i][j][k] > 3:
                        test_verdict = False
                        break
                elif images_1_components[i][j][k] < images_2_components[i][j][k]:
                    if images_2_components[i][j][k] - images_1_components[i][j][k] > 3:
                        test_verdict = False
                        break
            if not test_verdict:
                break
        if not test_verdict:
            break

    if test_verdict:
        print("test_result_image OK!")
    else:
        print("test_result_image FAILED! (at least one pixel in one of the RGB components differs "
              "by more than 3 of 256 for this two images)")


if __name__ == '__main__':
    test_result_image()
