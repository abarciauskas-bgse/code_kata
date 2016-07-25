def fast_exponentiation(a,n):
    """
    Computes a** in log(n) time using recursion and the fact that n = n/2 + n/2
    """
    if n == 0: return 1
    x = fast_exponentiation(a, n/2)
    if n % 2 == 0:
        return x**2
    else:
        return a*(x**2)
