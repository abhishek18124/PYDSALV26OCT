def is_prime(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            # n is not prime
            return False
        i += 1
    # n is prime
    return True


def print_primes(m: int) -> None:
    cnt = 0
    num = 2
    while True:
        if is_prime(num):
            print(num, end=" ")
            cnt += 1
            if cnt == m:
                break
        num += 1


m = int(input())
print_primes(m)
