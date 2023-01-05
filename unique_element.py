import numpy as np
from mergesort import merge_sort

def unique_element(some_list):
    """Get unique element in list where each element occurs exactly twice except one.

    Args:
        some_list (list): List of integers.

    Returns:
        int: unique element in list
    """
    ## check for invalid input
    if not all(isinstance(item, int) for item in some_list):
        return 'bruh'
    

    ## sort list
    merge_sort(some_list)
    ## check if first element is unique
    if some_list[0] != some_list[1]:
        return some_list[0]
    ## check if last element is unique
    elif some_list[-1] != some_list[-2]:
        return some_list[-1]
    else:
        ## check all other elements
        for i in range(1,len(some_list)-2):
            if some_list[i] != some_list[i+1] and some_list[i] != some_list[i-1]:
                return some_list[i]
            