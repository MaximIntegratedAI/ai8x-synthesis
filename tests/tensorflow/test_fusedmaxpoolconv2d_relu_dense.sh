#!/bin/sh
#./ai8xize.py --verbose -L --top-level cnn --test-dir tests/tensorflow --prefix fusedmaxpoolconv2d_relu_dense --checkpoint-file ../ai8x-training/TensorFlow/test/FusedMaxPoolConv2dReLU_Dense/saved_model/saved_model.onnx --config-file tests/tensorflow/simple-fusedmaxpoolconv2d-relu-dense.yaml --sample-input ../ai8x-training/TensorFlow/test/FusedMaxPoolConv2dReLU_Dense/saved_model/input_sample_1x8x8.npy --device 85 --compact-data --mexpress --embedded-code --scale 1.0 "$@"
./ai8xize.py --verbose -L --top-level cnn --test-dir tests/tensorflow --prefix fusedmaxpoolconv2d_relu_dense --checkpoint-file ../ai8x-training/TensorFlow/test/FusedMaxPoolConv2dReLU_Dense/saved_model/saved_model.onnx --config-file tests/tensorflow/simple-conv2d-relu-maxpool-dense.yaml --sample-input ../ai8x-training/TensorFlow/test/FusedMaxPoolConv2dReLU_Dense/saved_model/input_sample_1x8x8.npy --device 85 --compact-data --mexpress --embedded-code --scale 1.0 "$@"
