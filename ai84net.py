###################################################################################################
#
# Copyright (C) 2019 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Confidential
#
###################################################################################################
"""
Networks that fit into AI84

Optionally quantize/clamp activations
"""
import torch.nn as nn
import ai84


class AI84Net5(nn.Module):
    """
    5-Layer CNN that uses max parameters in AI84
    """
    def __init__(self, num_classes=10, num_channels=3, dimensions=(28, 28),
                 simulate=False, planes=60, pool=2, fc_inputs=12, bias=False):
        super(AI84Net5, self).__init__()

        # AI84 Limits
        assert planes + num_channels <= ai84.WEIGHT_INPUTS
        assert planes + fc_inputs <= ai84.WEIGHT_DEPTH-1
        assert pool == 2
        assert dimensions[0] == dimensions[1]  # Only square supported

        # Keep track of image dimensions so one constructor works for all image sizes
        dim = dimensions[0]

        self.conv1 = ai84.FusedConv2dReLU(num_channels, planes, 3,
                                          padding=1, bias=bias, simulate=simulate)
        # padding 1 -> no change in dimensions -> MNIST: 28x28 | CIFAR: 32x32

        pad = 2 if dim == 28 else 1
        self.conv2 = ai84.FusedMaxPoolConv2dReLU(planes, planes, 3, pool_size=2, pool_stride=2,
                                                 padding=pad, bias=bias, simulate=simulate)
        dim //= 2  # pooling, padding 0 -> MNIST: 14x14 | CIFAR: 16x16
        if pad == 2:
            dim += 2  # MNIST: padding 2 -> 16x16 | CIFAR: padding 1 -> 16x16

        self.conv3 = ai84.FusedMaxPoolConv2dReLU(planes, ai84.WEIGHT_DEPTH-planes-fc_inputs, 3,
                                                 pool_size=2, pool_stride=2, padding=1,
                                                 bias=bias, simulate=simulate)
        dim //= 2  # pooling, padding 0 -> 8x8
        # padding 1 -> no change in dimensions

        self.conv4 = ai84.FusedAvgPoolConv2dReLU(ai84.WEIGHT_DEPTH-planes-fc_inputs, fc_inputs, 3,
                                                 pool_size=pool, pool_stride=2, padding=1,
                                                 bias=bias, simulate=simulate)
        dim //= pool  # pooling, padding 0 -> 4x4
        # padding 1 -> no change in dimensions

        self.fc = ai84.SoftwareLinear(fc_inputs*dim*dim, num_classes, bias=True, simulate=simulate)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')

    def forward(self, x):  # pylint: disable=arguments-differ
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x


def ai84net5(pretrained=False, **kwargs):
    """
    Constructs a AI84Net5 model.
    """
    assert not pretrained
    return AI84Net5(**kwargs)


class AI84NetExtraSmall(nn.Module):
    """
    Minimal CNN that tries to achieve 1uJ per inference for MNIST
    """
    def __init__(self, num_classes=10, num_channels=3, dimensions=(28, 28),
                 simulate=False, fc_inputs=8, bias=False):
        super(AI84NetExtraSmall, self).__init__()

        # AI84 Limits
        assert dimensions[0] == dimensions[1]  # Only square supported

        # Keep track of image dimensions so one constructor works for all image sizes
        dim = dimensions[0]

        self.conv1 = ai84.FusedConv2dReLU(num_channels, 8, 3,
                                          padding=1, bias=bias, simulate=simulate)
        # padding 1 -> no change in dimensions -> 8x28x28

        pad = 2 if dim == 28 else 1
        self.conv2 = ai84.FusedMaxPoolConv2dReLU(8, 8, 3, pool_size=2, pool_stride=2,
                                                 padding=pad, bias=bias, simulate=simulate)
        dim //= 2  # pooling, padding 0 -> 8x14x14
        if pad == 2:
            dim += 2  # padding 2 -> 8x16x16

        self.conv3 = ai84.FusedMaxPoolConv2dReLU(8, fc_inputs, 3,
                                                 pool_size=4, pool_stride=4, padding=1,
                                                 bias=bias, simulate=simulate)
        dim //= 4  # pooling, padding 0 -> 8x4x4
        # padding 1 -> 8x4x4

        self.fc = ai84.SoftwareLinear(fc_inputs*dim*dim, num_classes, bias=True, simulate=simulate)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')

    def forward(self, x):  # pylint: disable=arguments-differ
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x


def ai84netextrasmall(pretrained=False, **kwargs):
    """
    Constructs a AI84NetExtraSmall model.
    """
    assert not pretrained
    return AI84NetExtraSmall(**kwargs)


class AI84NetSmall(nn.Module):
    """
    Minimal CNN that tries to achieve 1uJ per inference for MNIST
    """
    def __init__(self, num_classes=10, num_channels=3, dimensions=(28, 28),
                 simulate=False, fc_inputs=12, bias=False):
        super(AI84NetSmall, self).__init__()

        # AI84 Limits
        assert dimensions[0] == dimensions[1]  # Only square supported

        # Keep track of image dimensions so one constructor works for all image sizes
        dim = dimensions[0]

        self.conv1 = ai84.FusedConv2dReLU(num_channels, 16, 3,
                                          padding=1, bias=bias, simulate=simulate)
        # padding 1 -> no change in dimensions -> 16x28x28

        pad = 2 if dim == 28 else 1
        self.conv2 = ai84.FusedMaxPoolConv2dReLU(16, 16, 3, pool_size=2, pool_stride=2,
                                                 padding=pad, bias=bias, simulate=simulate)
        dim //= 2  # pooling, padding 0 -> 16x14x14
        if pad == 2:
            dim += 2  # padding 2 -> 16x16x16

        self.conv3 = ai84.FusedMaxPoolConv2dReLU(16, fc_inputs, 3,
                                                 pool_size=4, pool_stride=4, padding=1,
                                                 bias=bias, simulate=simulate)
        dim //= 4  # pooling, padding 0 -> 16x4x4
        # padding 1 -> 12x4x4

        self.fc = ai84.SoftwareLinear(fc_inputs*dim*dim, num_classes, bias=True, simulate=simulate)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')

    def forward(self, x):  # pylint: disable=arguments-differ
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x


def ai84netsmall(pretrained=False, **kwargs):
    """
    Constructs a AI84NetSmall model.
    """
    assert not pretrained
    return AI84NetSmall(**kwargs)
