#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum = 0
    ave = 0

    for lis in my_list:
        sum += lis[0] * lis[1]
        ave += lis[1]
    return (sum / ave)
