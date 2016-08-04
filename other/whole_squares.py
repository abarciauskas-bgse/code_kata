import math

def solution(A, B):
    # write your code in Python 2.7
    whole_squares = []
    for integer in range(A, B+1):
        if integer not in whole_squares:
            integer_sqrt = math.sqrt(integer)
            if integer_sqrt%1 == 0.0:
                whole_squares.append(integer)
                integer_squared = integer**2
                if integer_squared in range(A, B+1):
                    whole_squares.append(integer_squared)
    return len(whole_squares)
