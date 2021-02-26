#!/bin/sh
./ai8xize.py --verbose -L --top-level cnn --test-dir tests/tensorflow --prefix conv2dReluMaxPool --checkpoint-file ../ai8x-training/TensorFlow/test/FusedMaxPoolConv2DReLU_bias/saved_model/saved_model.onnx --config-file tests/tensorflow/simple-conv2dReluMaxPool.yaml --sample-input ../ai8x-training/TensorFlow/test/FusedMaxPoolConv2DReLU_bias/saved_model/input_sample_1x4x4.npy --device 85 --compact-data --mexpress --embedded-code --scale 1.0 "$@"
