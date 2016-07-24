# sorts last out of order item into ar[0:len(ar)-1], which is considered already sorted
#
def insertionSort(ar):
    out_of_order_item = ar[len(ar)-1]
    idcs = range(len(ar)-1)
    idcs.reverse()
    for i in idcs:
        current_item = ar[i]
        if current_item > out_of_order_item:
            ar[i+1] = current_item
            print ' '.join(map(str, ar))
            if i == 0:
                ar[i] = out_of_order_item
                print ' '.join(map(str, ar))
        else:
            ar[i+1] = out_of_order_item
            print ' '.join(map(str, ar))
            break
        if i == 0: ar[i]


# ar = '2 3 4 5 6 7 8 9 10 1'
# ar = map(int, ar.split())
# insertionSort(ar)

