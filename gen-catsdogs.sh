#!/bin/sh
./ai8xize.py -e --verbose --top-level cnn -L --test-dir demos --prefix cats-vs-dogs-chw --checkpoint-file trained/ai85-catsdogs-chw.pth.tar --config-file networks/cats-dogs-chw.yaml --device 85 --compact-data --mexpress --softmax --display-checkpoint --embedded-code --boost 2.5