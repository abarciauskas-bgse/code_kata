def partition(array, lo, hi):
    i = lo
    pivot_val = array[hi-1]
    for j in range(lo, hi-1):
        if array[j] < pivot_val:
            jval = array[j]
            ival = array[i]
            array[i] = jval
            array[j] = ival
            i += 1
    swapval = array[i]
    array[i] = pivot_val
    array[hi-1] = swapval
    return array, i

def quicksort(array, lo, hi):
    if lo < hi:
        array, pivot_index = partition(array, lo, hi)
        quicksort(array, lo, pivot_index)
        quicksort(array, pivot_index+1, hi)
    return array
