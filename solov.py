def jacobi(a, n):
    """Compute the Jacobi symbol for (a / n).

        Args_1:
            a, n (int): int to evaluate the jacobi function.
    """
    j = 1
    while a != 0:
        while a % 2 == 0:
            j *= pow(-1, (n * n - 1) / 8)
            a /= 2
        if not ((a - 3) % 4 or (n - 3) % 4):
            j = -j
        a, n = n, a
        a %= n
    return j


def gcd(a, b):
    """Compute the greater common divisor of to integer.

        Args_1:
            a, b (int): the number one wanna find the gcd.
    """
    while b:
        a, b = b, a % b
    return a


def test_solovay(n):
    """Implement the algorithm of Solovay-Strassen, which tells you if a given integer is probably a prime o certainly not.

        Args_1:
            n (int): the int to test.
    """
    for h in range(2, n):
        a = h
        if gcd(a, n) > 1:
            return False
        x = int(jacobi(a, n))
        e = int((n - 1) / 2)
        y = int(pow(a, e, n))
        if y == n - 1:
            y = -1
        if x != y:
            return False
    return True


if __name__ == "__main__":
    for i in range(2, 100):
        if test_solovay(i):
            print(i, "is probably prime")
        else:
            print(i, "is not prime")
