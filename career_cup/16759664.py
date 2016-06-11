# sort the integers in all the arrays mergesort / O(nlogn)
# call this new array sorted
# also need to adapt quick sort or merge sort to keep track of list positions
ksorted, kidx_of_sorted = mergesort(arr)
# requires numpy
min_range = [-inf, inf]
min_range_size = inf
current_offset = 0
while curent_offset < (len(ksorted) - k):
    new_range = []
    # keep track of what lists we have sourced from
    new_range_kidcs = []
    for i in range(current_offset, len(ksorted)):
        if kidx_of_sorted not in new_range_kidcs:
            new_range.append(ksorted[i])
            new_range_kidcs.append(kidx_of_sorted[i])
        if len(new_range_kidcs) == k: break
    current_offset += 1
    min_new_range = new_range[0]
    max_new_range = new_range[-1]
    new_range = [min_new_range, max_new_range]
    new_range_size = max_new_range - min_new_range
    if new_range_size < min_range_size:
        min_new_range = new_range
        min_new_range = new_range_size
