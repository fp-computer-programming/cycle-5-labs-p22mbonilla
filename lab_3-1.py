# Author MB 10/25/2021

import math
import time

t_start = time.process_time

math.pow(2, 2)

t_end = time.process_time

t_change = t_end - t_start

print(t_change)

t1 = time.perf_counter

2 ** 2

t2 = time.perf_counter

t_cool = t2 - t1

print(t_cool)
