#!/bin/sh
./ai8xize.py --verbose -L --top-level cnn --test-dir tests/tensorflow --prefix dense --checkpoint-file ../ai8x-training/TensorFlow/test/FusedDense/saved_model/saved_model.onnx --config-file tests/tensorflow/simple-dense.yaml --sample-input ../ai8x-training/TensorFlow/test/FusedDense/saved_model/input_sample_10x1.npy --device 85 --compact-data --mexpress --embedded-code --scale 1.0 "$@"
