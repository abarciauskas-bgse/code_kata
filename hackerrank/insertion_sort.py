# sorts last out of order item into ar[0:len(ar)-1], which is considered already sorted
#
def insert_item(ar):
    out_of_order_item = ar[len(ar)-1]
    idcs = range(len(ar)-1)
    idcs.reverse()
    for i in idcs:
        current_item = ar[i]
        if current_item > out_of_order_item:
            ar[i+1] = current_item
            if i == 0:
                ar[i] = out_of_order_item
        else:
            ar[i+1] = out_of_order_item
            break
        if i == 0: ar[i]
    return ar


# ar = '2 3 4 5 6 7 8 9 10 1'
# ar = map(int, ar.split())
# insertionSort(ar)

def insertion_sort(ar):
    already_sorted = [ar[0]]
    unsorted = ar[1:len(ar)]
    for item in unsorted:
        already_sorted.append(item)
        already_sorted = insert_item(already_sorted)
    return already_sorted
