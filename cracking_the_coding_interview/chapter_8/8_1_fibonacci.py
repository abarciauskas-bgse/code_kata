# Write a method to generate the nth Fibonacci number.
# Following the recommended approach:
# 1. What is the subproblem?
#    Adding two numbers
# 2. Solve for f(0): fib(0): return None
# 3. Solve for f(1): fib(1): return 1
# 4. Solve for f(2): fib(2): return fib(1) + 1
# 5. Understand how to use f(2) for f(3): f(3) = f(2) + sum(all previous numbers)
# 6. Generalize: Need to keep a list of integers summed so far, and we measure the length of that list,
# so pass the list to every recursive call plus the last sum and the number we are looking for
#
def fibonacci(n):
    if n == 0: return None
    if n == 1: return [1]
    numbers_so_far = [1, 1]
    return add_fib_int(n, numbers_so_far, 0)

def add_fib_int(n, numbers_so_far, last_sum):
    if n > len(numbers_so_far):
        last_sum = numbers_so_far[-1] + numbers_so_far[len(numbers_so_far)-2]
        numbers_so_far.append(last_sum)
        add_fib_int(n, numbers_so_far, last_sum)
    return numbers_so_far

print fibonacci(2)
