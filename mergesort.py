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

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
