def get_hourglass_sum(arr, row_idx, col_idx):
    top_row = arr[row_idx][col_idx:(col_idx+3)]
    middle_row = arr[row_idx+1][col_idx+1]
    bottom_row = arr[row_idx+2][col_idx:(col_idx+3)]
    all_values = top_row
    all_values.extend([middle_row])
    all_values.extend(bottom_row)
    return sum(all_values)

def max_hourglass(raw_input):
    arr = []
    raw_input = raw_input.split("\n")
    for arr_i in xrange(6):
        arr_temp = map(int,raw_input[arr_i].strip().split(' '))
        arr.append(arr_temp)    
    # for every row and col index in the viable range, check the sum of the corresponding hour glass
    # we have an array of arrays
    # the row index should go from 0 to len(arr)-3 (e.g. [0,1,2,3] in above example)
    # the col index should go from 0 to len(arr[0])-3
    row_range = xrange(len(arr)-2)
    col_range = xrange(len(arr[0])-2)
    max_sum = -float("inf")
    for row_idx in row_range:
        for col_idx in col_range:
            # get items for hour glass with origin at row_idx, col_idx
            hourglass_sum = get_hourglass_sum(arr, row_idx, col_idx)
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum

    return max_sum

