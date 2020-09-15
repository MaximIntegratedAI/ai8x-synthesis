#!/bin/sh
./ai8xize.py --verbose -L --top-level cnn --test-dir tests/tensorflow --prefix conv1d_relu_avgpool --checkpoint-file ../ai8x-training/TensorFlow/test/FusedAvgPoolConv1DReLU/saved_model/saved_model.onnx --config-file tests/tensorflow/simple-conv1d_relu_avgpool.yaml --sample-input ../ai8x-training/TensorFlow/test/FusedAvgPoolConv1DReLU/saved_model/input_sample_7x9.npy --device 85 --compact-data --mexpress --unload --embedded-code --keep-first --scale 1.0 $@
