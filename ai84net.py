###################################################################################################
#
# Copyright (C) 2019 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Confidential
#
###################################################################################################
"""
Network(s) that fit into AI84

Optionally quantize/clamp activations
"""
import torch.nn as nn
import ai84


__all__ = ['AI84Net5', 'ai84net5']


class AI84Net5(nn.Module):
    """
    CNN that uses max parameters in AI84
    """
    def __init__(self, num_classes=10, num_channels=3, dimensions=(28, 28),
                 quantize=False, clamp_range1=False,
                 planes=10, pool=4, fc_inputs=12, bias=False):
        super(AI84Net5, self).__init__()

        # AI84 Limits
        assert planes + num_channels <= ai84.WEIGHT_INPUTS
        assert planes + fc_inputs <= ai84.WEIGHT_DEPTH-1
        assert pool <= ai84.MAX_AVG_POOL
        assert dimensions[0] == dimensions[1]  # Only square supported

        self.clamp_range1 = clamp_range1
        self.quantize = quantize
        self.num_bits = 8

        # Keep track of image dimensions so one constructor works for all image sizes
        dim = dimensions[0]

        self.conv1 = nn.Conv2d(num_channels, planes, kernel_size=3,
                               stride=1, padding=2, bias=bias)
        dim += 2  # padding -> 30x30
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1 if pool == 3 else 0)
        if pool != 3:
            dim -= 2  # stride of 2 -> 14x14, else 15x15
        dim //= 2
        self.conv2 = nn.Conv2d(planes, planes, kernel_size=3,
                               stride=1, padding=1 if pool == 3 else 2, bias=bias)
        if pool != 3:
            dim += 2  # padding 2 -> 16x16, else 15x15
        self.conv3 = nn.Conv2d(planes, ai84.WEIGHT_DEPTH-planes-fc_inputs, kernel_size=3,
                               stride=1, padding=1, bias=bias)
        # no change in dimensions
        self.avgpool = nn.AvgPool2d(pool)
        dim //= pool  # pooling -> 4x4, else 3x3 or 5x5
        self.conv4 = nn.Conv2d(ai84.WEIGHT_DEPTH-planes-fc_inputs, fc_inputs, kernel_size=3,
                               stride=1, padding=1, bias=bias)
        # no change in dimensions
        self.fc = nn.Linear(fc_inputs*dim*dim, num_classes)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')

    def forward(self, x):  # pylint: disable=arguments-differ
        x = self.conv1(x)
        x = self.relu(x)
        if self.clamp_range1:
            x = x.clamp(min=-1., max=1.)
        elif self.quantize:
            x = x.add(.5).div(2**(self.num_bits-1)).floor().clamp(min=-(2**(self.num_bits-1)),
                                                                  max=2**(self.num_bits-1)-1)
        x = self.maxpool(x)
        x = self.conv2(x)
        x = self.relu(x)
        if self.clamp_range1:
            x = x.clamp(min=-1., max=1.)
        elif self.quantize:
            x = x.add(.5).div(2**(self.num_bits-1)).floor().clamp(min=-(2**(self.num_bits-1)),
                                                                  max=2**(self.num_bits-1)-1)
        x = self.conv3(x)
        x = self.relu(x)
        if self.clamp_range1:
            x = x.clamp(min=-1., max=1.)
        elif self.quantize:
            x = x.add(.5).div(2**(self.num_bits-1)).floor().clamp(min=-(2**(self.num_bits-1)),
                                                                  max=2**(self.num_bits-1)-1)
        x = self.avgpool(x)
        x = self.conv4(x)
        x = self.relu(x)
        if self.clamp_range1:
            x = x.clamp(min=-1., max=1.)
        elif self.quantize:
            x = x.add(.5).div(2**(self.num_bits-1)).floor().clamp(min=-(2**(self.num_bits-1)),
                                                                  max=2**(self.num_bits-1)-1)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x


def ai84net5(pretrained=False, **kwargs):
    """
    Constructs a AI84Net-5 model.
    """
    assert not pretrained
    return AI84Net5(**kwargs)
