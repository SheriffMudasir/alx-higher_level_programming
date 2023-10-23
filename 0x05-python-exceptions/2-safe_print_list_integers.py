#!/usr/bin/python
def safe_print_list_integers(my_list=[], x=0):
        try:
                num_count = 0
                for i in range(x):
                        if type(my_list[i]) is int:
                                print("{:d}".format(my_list[i]), end='')
                                num_count += 1
                print()
                                
                return num_count
        except IndexError:
                return num_count
