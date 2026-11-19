def is_prime(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            # n is not prime
            return False
        i += 1
    # n is prime
    return True


n = int(input())
print(is_prime(n))
