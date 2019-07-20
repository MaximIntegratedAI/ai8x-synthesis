#!/usr/bin/env python3
###################################################################################################
# Copyright (C) 2019 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Confidential
#
# Written by RM
###################################################################################################
"""
Test the linear operator.
"""
import numpy as np
import compute


def test_linear():
    """Main program to test compute.linear."""
    weight = np.array(
        [[-16, 26, 35, -6, -40, -31, -27, -54, -51, -84, -69, -65,
          -8, -8, -13, -16, -3, 33, 48, 39, 27, 56, 50, 57, 31, 35,
          2, 8, 16, 28, 13, -18, 8, -6, 32, 20, -3, 4, 42, 41, 3, 23,
          67, 74, 8, 29, 80, 54, -3, -12, -27, -29,
          -17, -5, -27, -5, -22, -19, -31, -5, 1, 10, -32, -38,
          -25, 0, 25, 32, -29, -44, -60, -49, -14, -22, -46, -47, -3, 1,
          -14, -8, -10, -2, 12, 24, -7, 24, -2, -10, 26, 62, 34, -7, 51,
          73, 34, 17, 3, 0, -28, -13, 14, 5, -28, -39,
          15, -25, -42, -31, 11, -37, -49, -27, 15, 27, 44, 38, 5, 9, 26,
          25, -36, -45, -20, -11, -35, -31, -9, -1, 4, -11,
          -3, 8, 2, 18, 7, 5, 29, 14, 9, -14, 6, 32, 19, 1, -2, 27, 29,
          34, -5, 42, 32, 32, 5, 18, 6, 13,
          -19, -36, 29, 48, 17, 14, -17, -17, -8, -33, -10, 20, -37,
          -36, 5, 20, -7, -5, 15, 7, -53, -27, 13, 17, -64, -81,
          -11, 15, -57, -99, -46, 23, -36, -58, -20, 20],
         [-30, -53, -38, -9, -6, -13, -17, 2, 16, -18, -15, 11, 19, 8, 31,
          27, 7, 25, 10, -4, 14, 55, 70, 20, -14, 14,
          35, 9, -1, -0, 6, 3, -23, -16, 4, 3, 23, 5, 20, 9, 53, 29, 17, 4,
          21, -2, -11, -3, -1, -3, -11, -16,
          -10, -24, -34, -27, -6, -17, -31, -36, -3, 3, -14, -15, -13, -19,
          -25, -10, -17, -11, -20, -20, -6, -8, -27, -29, -14, -23,
          -12, -4, -2, -7, -10, -12, 13, 12, 18, 2, 6, 30, 58, 25, -8, -1,
          20, 7, 6, 14, 31, 11, 30, 76, 106, 64,
          27, 105, 124, 85, 13, 57, 76, 45, -8, -12, -23, -26, 4, -7, -38,
          -46, 23, 14, -4, 7, 19, 23, -2, 8, 11, 9,
          8, 11, -36, -53, -18, 4, -33, -62, -62, -30, -27, -37, -33, -19,
          -4, -27, -30, -20, -9, -37, -52, -36, 2, 5, -30, -41,
          -7, 3, -10, -12, 5, 30, 22, 7, 31, 72, 25, -17, 13, 5, -63, -35,
          -1, -12, -35, -19, 2, 5, -5, -15, -8, 3,
          1, -15, -4, -2, -11, -8, -6, -17, -7, -6],
         [26, 8, -30, -14, -1, -1, 49, 37, 11, 23, 64, 42, 31, 19, 51, 46,
          -3, -0, -1, -5, -46, -52, -67, -55, -36, -43,
          -65, -62, 9, 18, 12, -19, 15, 20, 9, 3, 5, 31, 79, 39, -45,
          -12, 33, 28, -25, -14, 1, 14, -3, 2, -8, -5,
          18, 3, -28, -34, 30, 27, -28, -33, 31, 44, 25, 25, 61, 52, 26,
          -2, 42, 15, 4, 19, 56, 51, 22, 26, 9, 1,
          22, 17, -5, -28, 2, 1, -14, -32, -13, 9, -44, -9, 32, 49, -36,
          -4, 39, 38, -11, -41, -25, 5, -27, -34, 29, 48,
          -42, -80, -25, 10, -34, -51, -55, -30, -10, 1, -27, -9, -10, -17,
          -67, -46, -38, -64, -41, -3, -16, -33, -17, -2, -6, -2,
          20, 6, -9, 6, 23, 4, -27, -11, 23, 37, -35, -22, 8, 5, 6, -15, 3,
          -8, 46, 41, 76, 45, 27, 56, 66, 37,
          12, -9, -32, -23, 16, -18, -41, -13, 71, 40, 10, -25, 13, -14,
          -39, -62, -13, -8, -16, -23, 28, 63, 50, 30, 12, 43,
          -2, -31, -58, -34, -73, -94, -73, -79, -56, -50],
         [11, 19, 17, 4, 4, -17, -18, -19, 7, 22, -33, -48, 9, 13, -36,
          -35, -17, -18, -34, -26, 5, -23, -49, -31, 11, -11,
          -6, 18, -4, 0, 8, -0, 51, 69, 18, -14, 28, 47, 10, -5, 38, 42,
          15, -0, 39, 48, 25, 5, -2, -7, 28, 30,
          -7, 16, 43, 27, 1, 18, 36, 32, 3, -27, -35, -25, 42, 20, 27, 5,
          -5, -15, 10, 18, -28, -27, 16, 24, -23, 3,
          12, 20, 32, -27, -42, -36, -16, -34, -54, -26, -1, -21, -43,
          -27, 1, -19, -43, -9, 2, 8, 16, -1, -11, -4, -3, -14,
          -22, -37, -27, -42, -5, -36, -36, -25, -24, -60, -89, -52, 11,
          -23, -60, -28, 44, 54, 31, -1, 31, 27, 28, -2, -17, -15,
          7, 1, -28, -54, -57, -23, -43, -68, -74, -25, -28, -44, -42,
          -9, -2, 1, -3, -16, 29, 0, -18, -25, 29, 7, -39, -27,
          -19, -19, -2, 1, -5, -25, -26, -8, 56, 51, -27, -38, 28, 15,
          -13, -1, -4, -9, 0, 12, 43, 59, 54, 43, 8, 25,
          53, 65, -4, 42, 92, 67, 25, 71, 77, 38],
         [-1, -19, -31, -38, 45, 48, 12, -11, 21, 44, 17, -2, 4, 20, 4,
          -2, -0, -23, -41, -26, 6, -15, -41, -25, 13, -2,
          -19, -32, 13, -6, -26, -31, -31, -43, -62, -37, -28, -41, -81,
          -48, -14, -39, -75, -43, -7, -27, -88, -53, -9, -20, -22, -23,
          -19, -36, -29, -34, -27, -37, -46, -40, -23, -38, -30, -2, -28,
          -52, -46, -30, 0, -1, -6, -12, -14, -16, -21, -8, 15, 24,
          -2, -6, 9, 12, 18, 8, 50, 56, 75, 44, 31, 18, 9, 10, 17, 4, 5,
          11, 10, 22, 17, -1, 23, 22, -17, -18,
          11, 31, 1, 1, 23, 45, 34, 21, -28, -35, -11, -4, -24, -31, 5,
          9, -14, -24, -6, -3, -18, -30, -2, 3, -1, 39,
          24, 20, 25, 30, 30, 39, 28, 63, 69, 52, 33, 46, 23, 20, 49,
          53, 51, 15, 17, 46, 47, 25, 9, 19, 25, 19,
          15, 28, -5, -25, -10, -11, 25, 16, -70, -69, -13, -8, -19,
          4, 31, 0, 16, 40, 38, 10, 22, 11, -12, -25, 47, 39,
          20, -0, 35, 49, 19, 7, 21, 47, -1, -12],
         [2, -14, -27, 24, 34, 31, -13, -0, 13, 8, 20, 13, -10, 15, 12,
          -4, -10, -26, -26, -10, -15, -21, -29, -27, -4, -4,
          -16, 7, -9, -21, -23, 12, -34, -8, 19, 38, -27, 3, 12, 32, 5,
          34, 32, 24, 30, 65, 44, 16, 0, -2, 6, -4,
          11, 13, 13, -4, -8, 5, 32, 11, -25, -10, 10, 2, -20, -31, -61,
          -14, 9, 57, 78, 74, -13, 0, 23, 21, -13, -8,
          -12, -13, -8, 7, 19, 40, -16, 13, 55, 44, -27, -38, -20, -15,
          -21, -27, -26, -24, -8, 3, 8, 15, -5, -30, -19, 21,
          -17, -16, -30, -11, -13, -26, -21, -15, 43, 52, 68, 40, 28, 55,
          85, 66, 20, 44, 54, 24, 20, 23, 10, -4, 1, 12,
          -31, -39, -31, -54, -46, -31, -54, -79, -60, -49, -29, -44, -44,
          -36, -17, -16, -25, -15, -25, -32, -57, -39, -22, -21, -20, -6,
          -3, -2, 15, 27, -10, -1, 25, 21, -26, -20, 33, 55, -28, 7, 46,
          61, -6, 3, 32, 41, -27, -72, -104, -62, 26, -18,
          -58, -53, 69, 55, 33, 18, 45, 48, 48, 28],
         [-66, -103, -62, -18, -52, -42, 36, 55, -7, 4, 46, 46, 2, 20,
          42, 8, 48, 26, -10, -10, 47, 34, 4, 1, 34, 41,
          30, 23, 10, 43, 35, 39, -1, -35, -54, -27, -0, -16, -46,
          -37, 18, 6, -11, -13, 20, 24, 42, 12, -6, -8, 20, 31,
          -14, -16, 17, 50, 8, 14, 32, 49, 8, 25, 56, 42, -12, -9,
          -16, 8, 26, 75, 95, 57, 11, 49, 97, 58, -14, 11,
          62, 31, -14, 8, -20, -8, 40, 50, 18, 15, 58, 57, 50, 17,
          38, 37, 37, 19, 19, 28, 8, -10, 35, 24, -32, -37,
          23, -8, -49, -35, 18, 3, -18, -14, -32, -30, 16, 20,
          -25, -37, 9, 26, -43, -34, -8, -1, -41, -15, -3, -3, 25, 26,
          -46, -44, -8, -37, -74, -37, 11, -7, -29, -45, 21, 10,
          -12, -32, -19, -43, -41, -17, -37, -53, -11, 25, -13, -32, 31, 30,
          9, -7, 11, 19, -11, 7, 14, 10, -24, 2, -13, 6, -13, -10,
          2, -2, 7, 1, -4, -11, 14, -12, -43, -13, -22, -9,
          -14, 1, -38, -65, -53, -21, -29, -46, -25, -7],
         [34, 61, 60, 41, -6, -7, 5, 23, 0, 19, 6, 3, -22, -37, -63,
          -29, -27, -41, -8, 9, -32, -57, 1, 24, -19, -19,
          10, -1, -17, -28, -6, -10, 64, 89, 62, 24, 38, 53, 12, -5,
          -11, -12, -34, -34, -48, -79, -68, -32, -17, -52, -79, -41,
          -35, -66, -64, -41, -23, -43, -53, -34, -20, -20, 4, -8, -7,
          -4, 11, -1, -27, -20, -43, -50, -24, 1, -10, -25, -14, -12,
          -29, -29, 32, 13, 9, -28, -28, -69, -75, -66, -17, -54, -78,
          -43, -38, -36, -55, -46, 10, 32, 19, -6, -7, 17, 29, 5,
          17, 34, 46, 32, 10, 45, 67, 35, 32, 13, 25, 1, 8, 19, 40,
          8, -17, -14, -15, -15, -1, -1, 4, -4, -15, -33,
          -9, 14, 12, 42, 36, 11, 2, 41, 56, 31, -5, -6, 39, 43, 8,
          7, -2, 1, 39, 22, -12, -10, 7, -2, -12, 6,
          26, 38, 21, 3, -15, -17, -18, -16, 63, 58, 42, 33, 72, 72,
          59, 30, 31, 26, 1, 3, 0, -6, 24, 9, -24, 3,
          21, 18, -21, -21, -21, -27, 34, 17, -26, -25],
         [20, 39, 33, 5, -8, -23, -28, -21, -57, -76, -74, -25, -29,
          -71, -58, -4, -17, -26, -0, -2, -48, -47, 8, 6, -57, -40,
          36, 46, -5, 20, 59, 86, -32, -39, -20, -10, -11, -32,
          -22, -5, -41, -33, 3, -6, -34, -28, 34, 14, 11, 33, 32, 27,
          19, 27, 34, 22, 26, 26, 57, 41, 38, 45, 71, 49, -9, 13,
          13, -6, -11, -8, 15, 13, 22, 8, 34, 31, 21, 16,
          35, 23, -14, 19, 10, 16, -28, 9, -7, 5, -27, 6, 22, 20,
          -22, -7, 28, 8, -7, -23, -12, 2, -15, 10, 2, -24,
          -29, -25, -26, -28, -27, -36, -44, -10, 8, 9, -14, -16,
          12, 5, -43, -36, 62, 52, 6, -1, 31, 30, 3, 5, 0, -0,
          22, 5, 47, 69, 57, 13, 65, 95, 47, 20, 27, 40, 48, 31,
          -2, 20, 5, 9, -9, 5, -14, -23, -14, 3, -22, -38,
          -2, 6, 2, -15, -2, -8, 2, 0, -38, -40, -23, -13, -9,
          -39, -34, -12, -41, -72, -67, -39, 4, -18, 1, 10, 39, 7,
          3, 16, 42, 42, 46, 52, 10, -4, 27, 38],
         [18, 34, 41, 9, 28, 55, 3, -14, 46, 56, 35, 26, 4, 23, 29,
          11, 21, 51, 58, 34, 40, 70, 52, 28, 40, 29,
          -6, -16, -12, -54, -79, -61, -16, -34, -7, -1, -23, -56,
          -25, -20, -8, -39, -46, -37, -7, -15, -57, -26, 28, 68, 60, 30,
          54, 84, 75, 45, 19, 28, 35, 16, -14, -33, -53, -31, 10,
          27, 46, 16, 12, -46, -76, -51, 9, -34, -89, -49, 33, -12,
          -61, -32, -18, 5, 5, -4, 4, -31, -18, -19, -3, -49, -65,
          -31, 17, -19, -36, -23, -22, -44, -34, -1, -35, -86, -69, -4,
          17, 22, 25, 18, 5, 36, 47, 20, 7, 32, 13, 8, -7, 25,
          44, 20, -0, 16, 1, 1, 12, 7, -11, 3, -5, -26,
          6, 19, 28, 34, 44, 14, 21, 15, 21, 25, 36, 24, -5, -5,
          -15, -7, 14, 17, -47, -30, 7, 6, -31, -53, -5, 8,
          -11, -1, -29, -24, 13, 29, 14, 2, -56, -61, -26, -15,
          -21, 1, 8, -1, 18, 37, 34, 16, -31, -3, 20, 4, -17, -11,
          -10, -12, 36, 33, 15, -17, 7, 21, -15, -25]],
        dtype=np.int64)

    bias = np.array([0, 24, -12, -19, 13, 3, -7, -1, -3, 2], dtype=np.int64)

    data = np.array(
        [[[85, 112, 69, 78],
          [69, 81, 51, 65],
          [45, 24, 0, 20],
          [34, 0, 15, 30]],
         [[0, 0, 3, 8],
          [0, 0, 12, 47],
          [0, 0, 0, 8],
          [0, 2, 0, 0]],
         [[84, 127, 83, 70],
          [77, 99, 94, 61],
          [0, 0, 28, 24],
          [0, 0, 5, 2]],
         [[0, 0, 14, 9],
          [4, 0, 0, 4],
          [9, 0, 0, 0],
          [0, 0, 0, 0]],
         [[13, 26, 27, 41],
          [19, 0, 0, 0],
          [8, 0, 0, 0],
          [14, 23, 15, 3]],
         [[26, 20, 20, 0],
          [9, 0, 0, 0],
          [0, 0, 0, 0],
          [11, 12, 3, 9]],
         [[5, 78, 57, 0],
          [19, 108, 79, 26],
          [0, 80, 90, 74],
          [25, 91, 107, 87]],
         [[45, 57, 32, 12],
          [24, 10, 0, 0],
          [0, 0, 0, 0],
          [15, 34, 0, 0]],
         [[0, 0, 0, 0],
          [0, 0, 0, 61],
          [39, 80, 75, 60],
          [7, 9, 25, 9]],
         [[59, 58, 37, 0],
          [40, 23, 5, 6],
          [52, 42, 0, 0],
          [14, 0, 4, 8]],
         [[30, 35, 0, 0],
          [67, 106, 104, 52],
          [87, 127, 90, 40],
          [45, 64, 26, 23]],
         [[56, 108, 108, 45],
          [56, 100, 83, 39],
          [16, 23, 10, 0],
          [8, 0, 10, 0]]],
        dtype=np.int64).flatten()

    assert len(data) == 12*4*4
    assert len(bias) == weight.shape[0] == 10

    output = np.zeros(10, dtype=np.int64)

    print('Input:', data)

    output = compute.linear(data, weight, bias,
                            in_features=len(data), out_features=weight.shape[0], debug=True)

    print('Output before division:', output)
    output += 64
    output //= 128
    print('Output:', output)

    compare = np.array([-34711, 37520, 22738, 16559, 2293,
                        -48963, -85140, 136144, -38265, -9148])
    compare += 64
    compare //= 128

    print('Expected:', compare)
    print("SUCCESS" if np.array_equal(output, compare) else "*** FAILURE ***")

    assert np.array_equal(output, compare)


if __name__ == '__main__':
    test_linear()
