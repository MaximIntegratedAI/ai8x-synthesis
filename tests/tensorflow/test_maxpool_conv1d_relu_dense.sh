#!/bin/sh
./ai8xize.py --verbose -L --top-level cnn --test-dir tests/tensorflow --prefix maxpool_conv1d_relu_dense --checkpoint-file ../ai8x-training/TensorFlow/test/MaxPool_Conv1dReLU_Dense/saved_model/saved_model.onnx --config-file tests/tensorflow/simple-maxpool-conv1d-relu-dense.yaml --sample-input ../ai8x-training/TensorFlow/test/MaxPool_Conv1dReLU_Dense/saved_model/input_sample_7x7x1.npy --device 85 --compact-data --mexpress --embedded-code --scale 1.0 "$@"
