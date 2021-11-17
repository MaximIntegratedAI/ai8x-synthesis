###################################################################################################
# Copyright (C) 2021 Maxim Integrated Products Inc. All Rights Reserved.
#
# Maxim Integrated Products Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
###################################################################################################
"""
Configuration state for backends.
"""
from typing import Any, List, Optional

# These are the raw global state variables, initialized to None, False, 0, [], or their defaults.
# Defaults must not depend on any other module such as tc.
activation: List[Any] = []
allow_streaming: bool = False
apb_base: int = 0
api_filename: str = ''
auto_input_dim: List[List[int]] = []
avg_pool_rounding: bool = False
base_directory: str = ''
bias_group_map: List[Any] = []
bias: List[Any] = []
big_data: List[bool] = []
block_mode: bool = False
board_name: str = ''
boost: Optional[List[int]] = None
bypass: List[bool] = []
c_filename: str = ''
calcx4: List[bool] = []
clock_trim: Optional[List[int]] = None
compact_data: bool = False
compact_weights: bool = False
conv_groups: List[int] = []
data: Any = None
debug_computation: bool = False
debug_latency: bool = False
debug_new_streaming: bool = False
debug_snoop: bool = False
debug_wait: int = 1
debug: bool = False
defines_arm: str = ''
defines_riscv: str = ''
defines: str = ''
dilation: List[List[int]] = []
eclipse_includes: str = ''
eclipse_openocd_args: str = ''
eclipse_variables: str = ''
eltwise: List[bool] = []
embedded_code: bool = False
enable_delay: int = 0
ext_rdy: bool = False
fast_fifo_quad: bool = False
fast_fifo: bool = False
fifo_go: bool = False
fifo: bool = False
final_layer: int = -1
first_layer_used: int = 0
fixed_input: bool = False
flatten: List[bool] = []
forever: bool = False
generate_kat: bool = True
greedy_kernel_allocator: bool = True
ignore_bias_groups: bool = False
ignore_hw_limits: bool = False
in_offset: List[int] = []
in_sequences: List[Any] = []
increase_delta1: int = 0
increase_delta2: int = 0
increase_start: int = 0
init_tram: bool = False
input_channel_skip: List[int] = []
input_channels: List[int] = []
input_csv_format: int = 888
input_csv_period: int = 0
input_csv_retrace: int = 0
input_csv: Optional[str] = None
input_dim: List[List[int]] = []
input_fifo: bool = False
input_filename: str = ''
input_offset: List[Any] = []
input_pix_clk: int = 0
input_skip: List[int] = []
input_sync: bool = False
kernel_format: str = ''
kernel_size: List[List[int]] = []
layers: int = 0
legacy_kernels: bool = False
legacy_test: bool = False
link_layer: bool = False
log_filename: str = ''
log_intermediate: bool = False
log_pooling: bool = False
log: bool = False
max_count: Optional[int] = None
measure_energy: bool = False
mexpress: bool = False
mlator_chunk: int = 0
mlator_noverify = False
mlator: bool = False
narrow_chunk: int = 0
new_kernel_loader: bool = False
next_sequence: List[int] = []
no_error_stop: bool = False
oneshot: int = 0
operands: List[Any] = []
operator: List[Any] = []
out_offset: List[int] = []
output_channels: List[int] = []
output_dim: List[List[int]] = []
output_filename: str = ''
output_offset: List[int] = []
output_padding: List[List[int]] = []
output_processor_map: List[int] = []
output_shift: List[int] = []
output_width: List[int] = []
override_delta1: Optional[int] = None
override_delta2: Optional[int] = None
override_rollover: Optional[int] = None
override_start: Optional[int] = None
overwrite_ok: bool = False
overwrite: bool = False
padding: List[List[int]] = []
pipeline: bool = False
pll: bool = False
pool_average: List[bool] = []
pool_dilation: List[List[int]] = []
pool_first: List[bool] = []
pool_stride: List[List[int]] = []
pool: List[List[int]] = []
pooled_dim: List[List[int]] = []
powerdown: bool = False
prefix: str = ''
pretend_zero_sram: bool = False
prev_sequence: List[int] = []
processor_map: List[int] = []
quantization: List[int] = []
read_ahead: List[bool] = []
repeat_layers: int = 1
reshape_inputs: bool = False
result_filename: Optional[str] = None
result_numpy: Optional[str] = None
result_output: bool = False
riscv_cache: bool = False
riscv_debug: bool = False
riscv_exclusive: bool = False
riscv_flash: bool = False
riscv: bool = False
rtl_preload: bool = False
runtest_filename: str = ''
sample_filename: str = ''
simple1b: bool = False
simulated_sequence: List[Any] = []
sleep: bool = False
slow_load: bool = False
snoop_loop: bool = False
snoop_sequence: List[Any] = []
snoop: List[int] = []
softmax: bool = False
split: int = 1
start_layer: int = 0
stopstart: bool = False
streaming: List[bool] = []
stride: List[List[int]] = []
synthesize_input: Optional[int] = None
synthesize_words: int = 0
tcalc: List[bool] = []
test_dir: str = ''
timeout: Optional[int] = None
timer: Optional[int] = None
unload: bool = True
verbose_all: bool = False
verbose: bool = False
verify_kernels: bool = False
verify_writes: bool = False
weight_filename: str = ''
weight_start: int = 0
weights: List[Any] = []
wfi: bool = True
wide_chunk: int = 0
write_gap: List[int] = []
write_zero_regs: bool = False
zero_sram: bool = False
zero_unused: bool = False
