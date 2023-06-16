#!/bin/sh
DEVICE="MAX78002"
TARGET="sdk/Examples/$DEVICE/CNN"
COMMON_ARGS="--device $DEVICE --timer 0 --display-checkpoint --verbose"

python ai8xize.py --test-dir $TARGET --prefix mnist --checkpoint-file trained/ai85-mnist-qat8-q.pth.tar --config-file networks/mnist-chw-ai85.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix mnist-riscv --checkpoint-file trained/ai85-mnist-qat8-q.pth.tar --config-file networks/mnist-chw-ai85.yaml --softmax $COMMON_ARGS --riscv --riscv-debug "$@"
python ai8xize.py --test-dir $TARGET --prefix cifar-10 --checkpoint-file trained/ai85-cifar10-qat8-q.pth.tar --config-file networks/cifar10-nas.yaml --sample-input tests/sample_cifar-10.npy --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix cifar-100 --checkpoint-file trained/ai85-cifar100-qat8-q.pth.tar --config-file networks/cifar100-nas.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix cifar-100-mixed --checkpoint-file trained/ai85-cifar100-qat-mixed-q.pth.tar --config-file networks/cifar100-simple.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix cifar-100-simplewide2x-mixed --checkpoint-file trained/ai85-cifar100-simplenetwide2x-qat-mixed-q.pth.tar --config-file networks/cifar100-simplewide2x.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix cifar-100-residual --checkpoint-file trained/ai85-cifar100-residual-qat8-q.pth.tar --config-file networks/cifar100-ressimplenet.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix kws20_v3_1 --checkpoint-file trained/ai87-kws20_v3-qat8-q.pth.tar --config-file networks/ai87-kws20-v3-hwc.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix kws20_v2_1 --checkpoint-file trained/ai87-kws20_v2-qat8-q.pth.tar --config-file networks/ai87-kws20-v2-hwc.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix faceid --checkpoint-file trained/ai85-faceid-qat8-q.pth.tar --config-file networks/faceid.yaml --fifo $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix cats-dogs --checkpoint-file trained/ai85-catsdogs-qat8-q.pth.tar --config-file networks/cats-dogs-hwc-no-fifo.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix camvid_unet --checkpoint-file trained/ai85-camvid-unet-large-fakept-q.pth.tar --config-file networks/camvid-unet-large-fakept.yaml $COMMON_ARGS --overlap-data --mlator --no-unload --max-checklines 8192 "$@"
python ai8xize.py --test-dir $TARGET --prefix aisegment_unet --checkpoint-file trained/ai85-aisegment-unet-large-fakept-q.pth.tar --config-file networks/aisegment-unet-large-fakept.yaml $COMMON_ARGS --overlap-data --mlator --no-unload --max-checklines 8192 "$@"
python ai8xize.py --test-dir $TARGET --prefix svhn_tinierssd --checkpoint-file trained/ai85-svhn-tinierssd-qat8-q.pth.tar --config-file networks/svhn-tinierssd.yaml --overlap-data $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix cifar-100-effnet2 --checkpoint-file trained/ai87-cifar100-effnet2-qat8-q.pth.tar --config-file networks/ai87-cifar100-effnet2.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix cifar-100-mobilenet-v2-0.75 --checkpoint-file trained/ai87-cifar100-mobilenet-v2-0.75-qat8-q.pth.tar --config-file networks/ai87-cifar100-mobilenet-v2-0.75.yaml --softmax $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix imagenet --checkpoint-file trained/ai87-imagenet-effnet2-q.pth.tar --config-file networks/ai87-imagenet-effnet2.yaml $COMMON_ARGS "$@"
python ai8xize.py --test-dir $TARGET --prefix kinetics --checkpoint-file trained/ai85-kinetics-qat8-q.pth.tar --config-file networks/ai85-kinetics-actiontcn.yaml --overlap-data --softmax --zero-sram $COMMON_ARGS "$@"