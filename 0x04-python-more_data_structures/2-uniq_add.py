#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    unique_sum = 0
    for i in unique:
        unique_sum += i
    return unique_sum
