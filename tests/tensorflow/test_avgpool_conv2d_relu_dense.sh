#!/bin/sh
./ai8xize.py --verbose -L --top-level cnn --test-dir tests/tensorflow --prefix avgpool_conv2d_relu_dense  --checkpoint-file ../ai8x-training/TensorFlow/test/AvgPool_Conv2ReLU_Dense/saved_model/saved_model.onnx --config-file tests/tensorflow/simple-avgpool-conv2d-relu-dense.yaml --sample-input ../ai8x-training/TensorFlow/test/AvgPool_Conv2ReLU_Dense/saved_model/input_sample_1x8x8.npy --device 85 --compact-data --mexpress --embedded-code --scale 1.0 "$@"
