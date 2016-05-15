def partition(arr, lo, hi):
    if hi >= len(arr): hi = len(arr) - 1
    pivot = arr[lo]
    i = lo + 1
    j = lo + 1
    while j <= hi:
        next_item = arr[j]
        if next_item > pivot:
            j += 1
        elif next_item == pivot:
            j += 1
        else:
            swap_val = arr[i]
            arr[j] = swap_val
            arr[i] = pivot
            arr[i-1] = next_item
            i += 1
            j += 1
    return {'arr': arr, 'i': i-1}

def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)['i']
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)
    return arr
