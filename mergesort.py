def merge_sort(list_to_sort_by_merge):
    """Sort array by merge sort algorithm.

    Args:
        list_to_sort_by_merge (list): Unsorted list that will be sorted in the end.
    """
    if (len(list_to_sort_by_merge) > 1):
        ## divide list in the middle
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        ## recursive call
        merge_sort(left)
        merge_sort(right)

        left_index = 0
        right_index = 0
        list_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                list_to_sort_by_merge[list_index] = left[left_index]
                left_index += 1
            else:
                list_to_sort_by_merge[list_index] = right[right_index]
                right_index += 1
            list_index += 1

        while left_index < len(left):
            list_to_sort_by_merge[list_index] = left[left_index]
            left_index += 1
            list_index += 1

        while right_index < len(right):
            list_to_sort_by_merge[list_index] = right[right_index]
            right_index += 1
            list_index += 1


import matplotlib.pyplot as plt
import numpy as np

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = np.array(range(len(my_list)))

plt.figure()
plt.bar(x-0.15, my_list, color='red', alpha=0.5, label="unsorted", width=0.3)
mergeSort(my_list)
plt.bar(x+0.15, my_list, color='green', alpha=0.5, label="sorted", width=0.3)
plt.legend()
plt.xlabel("Position within list")
plt.show()
