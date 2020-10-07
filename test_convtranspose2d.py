#!/usr/bin/env python3
###################################################################################################
# Copyright (C) Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
###################################################################################################
"""
Test the convtranspose2d operator.
"""
import numpy as np
import torch
import compute


def deconvolve(groups, data, weight, expected):
    """Upsample data"""
    print('Input:\n', data)

    wflip = np.flip(weight, axis=(2, 3)).swapaxes(0, 1)
    wunflip = np.flip(wflip, axis=(2, 3)).swapaxes(0, 1)
    assert np.array_equal(wunflip, weight)

    t = torch.nn.functional.conv_transpose2d(
        torch.as_tensor(data, dtype=torch.float).unsqueeze(0),
        torch.as_tensor(np.flip(weight, axis=(2, 3)).swapaxes(0, 1).copy(), dtype=torch.float),
        bias=None,
        stride=2,
        padding=1,
        output_padding=1,
        groups=groups,
        dilation=1,
    ).int().squeeze().numpy()

    if groups > 1:
        weight = weight.transpose(1, 0, 2, 3)

    output = compute.conv2d(
        data,
        weight,
        None,
        data.shape,
        expected.shape,
        kernel_size=[3, 3],
        stride=[1, 1],
        pad=[1, 1],
        dilation=[1, 1],
        fractional_stride=[2, 2],
        output_pad=[0, 0],
        groups=groups,
        debug=True,
    )

    print("PYTORCH OK" if np.array_equal(output, t) else "*** FAILURE ***")
    assert np.array_equal(output, t)

    print('Output before division:\n', output)
    output += 64
    output //= 128
    print('Output:\n', output)

    print('Expected:\n', expected)
    print("SUCCESS" if np.array_equal(output, expected) else "*** FAILURE ***")
    assert np.array_equal(output, expected)


def test_convtranspose2d():
    """Main program to test compute.conv2d with fractional stride."""

    # 3x4x4 (CHW)
    d0 = np.array(
        [[[-41, -98, 16, 73],
          [49, 73, 28, 25],
          [35, 104, -27, -107],
          [111, 42, -46, -10]],
         [[-114, -28, -31, 21],
          [103, -76, 27, 78],
          [-51, -74, 57, -76],
          [-126, -71, 17, -40]],
         [[-98, 31, 109, 33],
          [-59, 86, -51, 69],
          [1, 85, -95, 121],
          [-93, 8, -103, 73]]],
        dtype=np.int64,
    )

    # 3x5x3x3
    w0 = np.array(
        [[[[-54, -64, 14],
           [52, -44, -60],
           [-90, -52, 42]],
          [[1, -77, 58],
           [25, 108, -18],
           [-30, 113, 37]],
          [[33, 90, 123],
           [-82, -17, 17],
           [55, -29, 102]]],
         [[[-104, -48, 34],
           [-41, 8, 11],
           [33, 96, 79]],
          [[11, 111, -65],
           [-82, 121, 94],
           [-49, -67, -29]],
          [[-81, 96, -89],
           [-109, -109, 98],
           [-46, 41, 99]]],
         [[[-67, 51, 43],
           [-7, -12, 118],
           [102, -68, 54]],
          [[102, -110, -127],
           [49, 14, 36],
           [-26, -23, -7]],
          [[-76, -56, 19],
           [49, -79, -79],
           [112, 52, 1]]],
         [[[62, -23, 31],
           [15, -50, -46],
           [72, 36, -53]],
          [[-62, -100, 31],
           [24, -108, 81],
           [-72, 85, 30]],
          [[-11, 62, 44],
           [70, 78, -108],
           [-45, -50, 87]]],
         [[[-85, -107, 3],
           [-90, -112, 47],
           [-74, -101, 71]],
          [[86, 111, -18],
           [6, 72, -99],
           [54, -76, -114]],
          [[110, 105, 56],
           [-81, -9, 69],
           [121, -69, -10]]]],
        dtype=np.int64,
    )

    # 5x8x8
    e0 = np.array(
        [[[-69, 78, 6, -54, -46, -102, -12, 13],
          [105, -16, -29, 121, 111, 108, 17, -28],
          [78, 66, -101, -64, 20, 36, 48, -19],
          [-187, 89, -57, -130, 17, 84, -62, 153],
          [-55, -23, -109, -35, 70, 138, -43, -136],
          [-121, -44, -29, -193, -31, 85, 137, 124],
          [-132, 71, -75, 4, 44, 71, -40, -59],
          [-45, -92, 27, -113, -60, 44, 80, 23]],
         [[-27, 164, -59, 85, -121, -31, -4, -65],
          [-193, 175, 158, -9, 39, -33, 16, -127],
          [151, -15, -141, -65, 71, 129, 17, -117],
          [80, 179, 115, -170, -106, -19, 108, -99],
          [-47, 40, -136, -91, 133, 81, -182, -20],
          [63, 131, 32, -191, -88, 91, 102, -10],
          [-33, 82, -71, -45, 101, 117, -101, -33],
          [-221, -1, -71, 5, -45, 71, 24, -42]],
         [[52, -196, -13, -55, -72, 82, -25, 17],
          [56, -10, -19, 222, -55, -110, -3, 23],
          [43, 7, -68, 65, 32, -8, -36, 55],
          [-52, 292, 49, -18, -24, -178, 32, 44],
          [-9, 2, -70, 48, 67, -208, -73, 23],
          [-17, 116, 62, -210, -39, 42, 12, -12],
          [33, -76, -17, 0, 70, -96, -48, 13],
          [193, -18, 74, -131, 12, 146, -2, -70]],
         [[52, -88, 81, -117, 86, 15, -26, 31],
          [154, 25, -9, 11, 120, 121, 18, -32],
          [-142, -154, 88, 91, -65, -37, -34, 55],
          [-142, 53, 35, 91, 17, 148, -160, -92],
          [30, -161, 74, 171, -95, -156, 180, 39],
          [18, 215, 42, 67, -47, 10, 79, -34],
          [6, -128, 48, 110, -59, -142, 82, 31],
          [33, 119, 52, 12, -55, -9, 68, 8]],
         [[-21, 88, 68, 137, -39, -53, -54, -71],
          [-213, -58, 24, 128, 39, -39, -119, 78],
          [19, 140, -113, -147, -6, 0, 17, -58],
          [2, 112, -140, -120, -3, -76, 168, 239],
          [-59, 114, -139, -236, 62, 166, 42, -5],
          [-35, -126, -77, -175, 76, -4, 115, 182],
          [-161, 50, -77, -123, 57, 165, -19, -41],
          [-278, -224, -90, -117, -31, -9, 34, 43]]],
        dtype=np.int64,
    )

    deconvolve(1, d0, w0, e0)

    d1 = np.array(
        [[[-41, -98],
          [49, 73]],
         [[-98, 31],
          [-59, 86]]],
        dtype=np.int64,
    )

    w1 = np.array(
        [[[[-54, -64, 14],
           [52, -44, -60],
           [-90, -52, 42]],
          [[33, 90, 123],
           [-82, -17, 17],
           [55, -29, 102]]],
         [[[-104, -48, 34],
           [-41, 8, 11],
           [33, 96, 79]],
          [[-81, 96, -89],
           [-109, -109, 98],
           [-46, 41, 99]]],
         [[[-67, 51, 43],
           [-7, -12, 118],
           [102, -68, 54]],
          [[110, 105, 56],
           [-81, -9, 69],
           [121, -69, -10]]]],
        dtype=np.int64,
    )

    e1 = np.array(
        [[[27, 96, 30, -60],
          [-55, 44, 22, 35],
          [-9, 35, -37, -25],
          [-66, 55, 24, -9]],
         [[81, 112, -33, 5],
          [-40, 193, 142, 48],
          [53, 107, -69, -97],
          [-63, -43, 37, -114]],
         [[11, -9, 7, -14],
          [-91, -75, -99, 217],
          [0, 148, -13, -58],
          [-29, -14, 100, 36]]],
        dtype=np.int64,
    )

    deconvolve(1, d1, w1, e1)

    d2 = np.array(
        [[[-41, -98],
          [49, 73]],
         [[-98, 31],
          [-59, 86]]],
        dtype=np.int64,
    )

    w2 = np.array(
        [[[[-54, -64, 14],
           [52, -44, -60],
           [-90, -52, 42]],
          [[-67, 51, 43],
           [-7, -12, 118],
           [102, -68, 54]]]],
        dtype=np.int64,
    )

    e2 = np.array(
        [[[14, 29, 34, -40],
          [1, -4, 19, -10],
          [-17, -14, -25, 30],
          [-24, -13, -36, -31]],
         [[9, 34, -3, -2],
          [-8, 51, -33, 52],
          [6, 83, -8, -5],
          [-24, 60, 34, -45]]],
        dtype=np.int64,
    )

    deconvolve(2, d2, w2, e2)


if __name__ == '__main__':
    test_convtranspose2d()
