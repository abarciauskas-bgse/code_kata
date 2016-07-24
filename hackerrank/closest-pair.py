n = int(raw_input().strip())
integers = map(int, raw_input().strip().split(' '))

integers.sort()

min_difference = float("inf")
pairs = []

for i in range(n-1):
    first_int = integers[i]
    second_int = integers[i+1]
    difference = abs(first_int - second_int)
    if difference < min_difference:
        min_difference = difference
        pairs = [first_int, second_int]
    elif difference == min_difference:
        if first_int not in pairs: pairs.append(first_int)
        pairs.append(second_int)
        
print(' '.join(map(str, pairs)))
