def recursiveAddition(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursiveAddition(arr[1:])

print recursiveAddition([1,2,3,4,5])
