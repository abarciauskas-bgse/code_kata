def merge(left, right):
    i = 0 # left pointer
    j = 0 # right pointer
    sorted_array = []
    if len(left) > 0 and len(right) > 0:
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
    if i < len(left):
        sorted_array = sorted_array + left[i:len(left)]                    
    if j < len(right):
        sorted_array = sorted_array + right[j:len(right)]
    return sorted_array

# # test
# l1 = [3,5,6]
# l2 = [2,4,7]
# merge(l1, l2)

import math

def merge_sort(array):
    left = []
    right = []
    final = []
    if len(array) > 1:
        left_end = int(math.floor(float(len(array))/2))
        right_start = int(math.ceil(float(len(array))/2))
        left_half = array[0:left_end]
        right_half = array[right_start:len(array)]
        left = merge_sort(left_half)
        right = merge_sort(right_half)
    else:
        return array
    return merge(left, right)        

# test
import random

#arr = [random.randint(1,10) for i in range(8)]
arr = random.sample(range(21),  8)
fin = merge_sort(arr)
print 'final is: ' + str(fin)
