"""
import keyword

print(keyword.iskeyword("for"))
print(keyword.iskeyword("soccer"))

import random
import statistics

num_list = []
for i in range (0,100):
    num_list.append(random.randint(0,100))
print (num_list)

print(statistics.mean(num_list))

print(statistics.median_high(num_list))

print(statistics.median_low(num_list))
"""
import cubed
print(cubed.cubed_cube(1))
print(cubed.cubed_cube(2))

print(cubed.cubed_cube(2000))
