#!/bin/sh

./ai8xize.py --verbose -L --top-level cnn --test-dir tensorflow --prefix tf-mnist --checkpoint-file ../ai8x-training/TensorFlow/export/mnist/saved_model.onnx --config-file ./networks/mnist-chw-ai85-tf.yaml --sample-input ../ai8x-training/TensorFlow/export/mnist/sampledata.npy --device MAX78000 --compact-data --mexpress --embedded-code --scale 1.0 --softmax --display-checkpoint $@

./ai8xize.py --verbose -L --top-level cnn --test-dir tensorflow --prefix tf-fashionmnist --checkpoint-file ../ai8x-training/TensorFlow/export/fashionmnist/saved_model.onnx --config-file ./networks/fashionmnist-chw-tf.yaml --sample-input ../ai8x-training/TensorFlow/export/fashionmnist/sampledata.npy --device MAX78000 --compact-data --mexpress --embedded-code --scale 1.0 --softmax --display-checkpoint $@

./ai8xize.py --verbose -L --top-level cnn --test-dir tensorflow --prefix tf-cifar10 --checkpoint-file ../ai8x-training/TensorFlow/export/cifar10/saved_model.onnx --config-file ./networks/cifar10-hwc-ai85-tf.yaml --sample-input ../ai8x-training/TensorFlow/export/cifar10/sampledata.npy --device MAX78000 --compact-data --mexpress --embedded-code --scale 1.0 --softmax --display-checkpoint $@

./ai8xize.py --verbose -L --top-level cnn --test-dir tensorflow --prefix tf-cifar100 --checkpoint-file ../ai8x-training/TensorFlow/export/cifar100/saved_model.onnx --config-file ./networks/cifar100-chw-tf.yaml --sample-input ../ai8x-training/TensorFlow/export/cifar100/sampledata.npy --device MAX78000 --compact-data --mexpress --embedded-code --scale 1.0 --softmax --display-checkpoint $@

./ai8xize.py --verbose -L --top-level cnn --test-dir tensorflow --prefix tf-kws20 --checkpoint-file ../ai8x-training/TensorFlow/export/kws20/saved_model.onnx --config-file ./networks/kws20-hwc-tf.yaml --sample-input ../ai8x-training/TensorFlow/export/kws20/sampledata.npy --device MAX78000 --compact-data --mexpress --embedded-code --scale 1.0 --softmax --display-checkpoint $@

./ai8xize.py --verbose -L --top-level cnn --test-dir tensorflow --prefix tf-rock --checkpoint-file ../ai8x-training/TensorFlow/export/rock/saved_model.onnx --config-file ./networks/rock-chw-tf.yaml --sample-input ../ai8x-training/TensorFlow/export/rock/sampledata.npy --device MAX78000 --compact-data --mexpress --embedded-code --scale 1.0 --softmax --display-checkpoint $@