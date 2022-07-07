#!/usr/bin/python3
import math
import sys

arr = [1, 4, 2, 3, 8, 7, 9]
max_ending_here = 0
max_so_far = -sys.maxsize
for i in range(0, len(arr)):
    max_ending_here = arr[i] + max_ending_here
    if(max_so_far < max_ending_here):
        max_so_far = max_ending_here
    if(max_so_far < 0):
        max_ending_here = 0

print(max_so_far)
