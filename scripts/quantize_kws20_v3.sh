#!/bin/sh
python3 quantize.py trained/ai85-kws20_v3-qat8.pth.tar trained/ai85-kws20_v3-qat8-q.pth.tar --device MAX78000 -v "$@"
