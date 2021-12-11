/*******************************************************************************
* Copyright (C) 2019-2021 Maxim Integrated Products, Inc., All rights Reserved.
*
* This software is protected by copyright laws of the United States and
* of foreign countries. This material may also be protected by patent laws
* and technology transfer regulations of the United States and of foreign
* countries. This software is furnished under a license agreement and/or a
* nondisclosure agreement and may only be used or reproduced in accordance
* with the terms of those agreements. Dissemination of this information to
* any party or parties not specified in the license agreement and/or
* nondisclosure agreement is expressly prohibited.
*
* The above copyright notice and this permission notice shall be included
* in all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
* OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
* IN NO EVENT SHALL MAXIM INTEGRATED BE LIABLE FOR ANY CLAIM, DAMAGES
* OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
* ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
* OTHER DEALINGS IN THE SOFTWARE.
*
* Except as contained in this notice, the name of Maxim Integrated
* Products, Inc. shall not be used except as stated in the Maxim Integrated
* Products, Inc. Branding Policy.
*
* The mere transfer of this software does not imply any licenses
* of trade secrets, proprietary technology, copyrights, patents,
* trademarks, maskwork rights, or any other form of intellectual
* property whatsoever. Maxim Integrated Products, Inc. retains all
* ownership rights.
*******************************************************************************/

// kws20_v3
// Created using ai8xize.py --test-dir test-Examples/MAX78000/CNN --prefix kws20_v3 --checkpoint-file trained/ai85-kws20_v3-qat8-q.pth.tar --config-file networks/kws20-v3-hwc.yaml --softmax --overwrite --device MAX78000 --compact-data --mexpress --timer 0 --display-checkpoint --verbose

#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include "mxc.h"
#include "cnn.h"
#include "sampledata.h"
#include "sampleoutput.h"

volatile uint32_t cnn_time; // Stopwatch

void fail(void)
{
  printf("\n*** FAIL ***\n\n");
  while (1);
}

// 128-channel 128x1 data input (16384 bytes total / 128 bytes per channel):
// HWC 128x1, channels 0 to 3
// HWC 128x1, channels 64 to 67
static const uint32_t input_0[] = SAMPLE_INPUT_0;

// HWC 128x1, channels 4 to 7
// HWC 128x1, channels 68 to 71
static const uint32_t input_4[] = SAMPLE_INPUT_4;

// HWC 128x1, channels 8 to 11
// HWC 128x1, channels 72 to 75
static const uint32_t input_8[] = SAMPLE_INPUT_8;

// HWC 128x1, channels 12 to 15
// HWC 128x1, channels 76 to 79
static const uint32_t input_12[] = SAMPLE_INPUT_12;

// HWC 128x1, channels 16 to 19
// HWC 128x1, channels 80 to 83
static const uint32_t input_16[] = SAMPLE_INPUT_16;

// HWC 128x1, channels 20 to 23
// HWC 128x1, channels 84 to 87
static const uint32_t input_20[] = SAMPLE_INPUT_20;

// HWC 128x1, channels 24 to 27
// HWC 128x1, channels 88 to 91
static const uint32_t input_24[] = SAMPLE_INPUT_24;

// HWC 128x1, channels 28 to 31
// HWC 128x1, channels 92 to 95
static const uint32_t input_28[] = SAMPLE_INPUT_28;

// HWC 128x1, channels 32 to 35
// HWC 128x1, channels 96 to 99
static const uint32_t input_32[] = SAMPLE_INPUT_32;

// HWC 128x1, channels 36 to 39
// HWC 128x1, channels 100 to 103
static const uint32_t input_36[] = SAMPLE_INPUT_36;

// HWC 128x1, channels 40 to 43
// HWC 128x1, channels 104 to 107
static const uint32_t input_40[] = SAMPLE_INPUT_40;

// HWC 128x1, channels 44 to 47
// HWC 128x1, channels 108 to 111
static const uint32_t input_44[] = SAMPLE_INPUT_44;

// HWC 128x1, channels 48 to 51
// HWC 128x1, channels 112 to 115
static const uint32_t input_48[] = SAMPLE_INPUT_48;

// HWC 128x1, channels 52 to 55
// HWC 128x1, channels 116 to 119
static const uint32_t input_52[] = SAMPLE_INPUT_52;

// HWC 128x1, channels 56 to 59
// HWC 128x1, channels 120 to 123
static const uint32_t input_56[] = SAMPLE_INPUT_56;

// HWC 128x1, channels 60 to 63
// HWC 128x1, channels 124 to 127
static const uint32_t input_60[] = SAMPLE_INPUT_60;

void load_input(void)
{
  // This function loads the sample data input -- replace with actual data

  memcpy32((uint32_t *) 0x50400000, input_0, 256);
  memcpy32((uint32_t *) 0x50408000, input_4, 256);
  memcpy32((uint32_t *) 0x50410000, input_8, 256);
  memcpy32((uint32_t *) 0x50418000, input_12, 256);
  memcpy32((uint32_t *) 0x50800000, input_16, 256);
  memcpy32((uint32_t *) 0x50808000, input_20, 256);
  memcpy32((uint32_t *) 0x50810000, input_24, 256);
  memcpy32((uint32_t *) 0x50818000, input_28, 256);
  memcpy32((uint32_t *) 0x50c00000, input_32, 256);
  memcpy32((uint32_t *) 0x50c08000, input_36, 256);
  memcpy32((uint32_t *) 0x50c10000, input_40, 256);
  memcpy32((uint32_t *) 0x50c18000, input_44, 256);
  memcpy32((uint32_t *) 0x51000000, input_48, 256);
  memcpy32((uint32_t *) 0x51008000, input_52, 256);
  memcpy32((uint32_t *) 0x51010000, input_56, 256);
  memcpy32((uint32_t *) 0x51018000, input_60, 256);
}

// Expected output of layer 8 for kws20_v3 given the sample input (known-answer test)
// Delete this function for production code
static const uint32_t sample_output[] = SAMPLE_OUTPUT;
int check_output(void)
{
  int i;
  uint32_t mask, len;
  volatile uint32_t *addr;
  const uint32_t *ptr = sample_output;

  while ((addr = (volatile uint32_t *) *ptr++) != 0) {
    mask = *ptr++;
    len = *ptr++;
    for (i = 0; i < len; i++)
      if ((*addr++ & mask) != *ptr++) {
        printf("Data mismatch (%d/%d) at address 0x%08x: Expected 0x%08x, read 0x%08x.\n",
               i + 1, len, addr - 1, *(ptr - 1), *(addr - 1) & mask);
        return CNN_FAIL;
      }
  }

  return CNN_OK;
}

// Classification layer:
static int32_t ml_data[CNN_NUM_OUTPUTS];
static q15_t ml_softmax[CNN_NUM_OUTPUTS];

void softmax_layer(void)
{
  cnn_unload((uint32_t *) ml_data);
  softmax_q17p14_q15((const q31_t *) ml_data, CNN_NUM_OUTPUTS, ml_softmax);
}

int main(void)
{
  int i;
  int digs, tens;

  MXC_ICC_Enable(MXC_ICC0); // Enable cache

  // Switch to 100 MHz clock
  MXC_SYS_Clock_Select(MXC_SYS_CLOCK_IPO);
  SystemCoreClockUpdate();

  printf("Waiting...\n");

  // DO NOT DELETE THIS LINE:
  MXC_Delay(SEC(2)); // Let debugger interrupt if needed

  // Enable peripheral, enable CNN interrupt, turn on CNN clock
  // CNN clock: 50 MHz div 1
  cnn_enable(MXC_S_GCR_PCLKDIV_CNNCLKSEL_PCLK, MXC_S_GCR_PCLKDIV_CNNCLKDIV_DIV1);

  printf("\n*** CNN Inference Test ***\n");

  cnn_init(); // Bring state machine into consistent state
  cnn_load_weights(); // Load kernels
  cnn_load_bias(); // Not used in this network
  cnn_configure(); // Configure state machine
  load_input(); // Load data input
  cnn_start(); // Start CNN processing

  SCB->SCR &= ~SCB_SCR_SLEEPDEEP_Msk; // SLEEPDEEP=0
  while (cnn_time == 0)
    __WFI(); // Wait for CNN

  if (check_output() != CNN_OK) fail();
  softmax_layer();

  printf("\n*** PASS ***\n\n");

#ifdef CNN_INFERENCE_TIMER
  printf("Approximate inference time: %u us\n\n", cnn_time);
#endif

  cnn_disable(); // Shut down CNN clock, disable peripheral

  printf("Classification results:\n");
  for (i = 0; i < CNN_NUM_OUTPUTS; i++) {
    digs = (1000 * ml_softmax[i] + 0x4000) >> 15;
    tens = digs % 10;
    digs = digs / 10;
    printf("[%7d] -> Class %d: %d.%d%%\n", ml_data[i], i, digs, tens);
  }

  return 0;
}

/*
  SUMMARY OF OPS
  Hardware: 8,402,528 ops (8,345,344 macc; 54,496 comp; 2,688 add; 0 mul; 0 bitwise)
    Layer 0: 1,651,200 ops (1,638,400 macc; 12,800 comp; 0 add; 0 mul; 0 bitwise)
    Layer 1: 3,640,896 ops (3,628,800 macc; 12,096 comp; 0 add; 0 mul; 0 bitwise)
    Layer 2: 1,177,344 ops (1,161,216 macc; 16,128 comp; 0 add; 0 mul; 0 bitwise)
    Layer 3: 565,104 ops (562,176 macc; 2,928 comp; 0 add; 0 mul; 0 bitwise)
    Layer 4: 281,280 ops (276,480 macc; 4,800 comp; 0 add; 0 mul; 0 bitwise)
    Layer 5: 518,784 ops (516,096 macc; 2,688 comp; 0 add; 0 mul; 0 bitwise)
    Layer 6: 407,288 ops (403,200 macc; 1,400 comp; 2,688 add; 0 mul; 0 bitwise)
    Layer 7: 155,256 ops (153,600 macc; 1,656 comp; 0 add; 0 mul; 0 bitwise)
    Layer 8: 5,376 ops (5,376 macc; 0 comp; 0 add; 0 mul; 0 bitwise)

  RESOURCE USAGE
  Weight memory: 169,472 bytes out of 442,368 bytes total (38%)
  Bias memory:   0 bytes out of 2,048 bytes total (0%)
*/

