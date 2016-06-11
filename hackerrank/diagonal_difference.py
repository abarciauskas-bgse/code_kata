#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

# sum every item on the first diagonal
first_sum = 0
for a_i in xrange(n):
    first_sum += a[a_i][a_i]
    
# sum every item on the second diagonal
second_sum = 0
# here we want the opposite position, in the first array we want the last item
for a_i in xrange(n):
    second_sum += a[a_i][n-a_i]

diff = first_sum - second_sum
diff = diff if diff > 0 else -diff

print diff
