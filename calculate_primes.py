import time


def gen_primes(known_primes=None, boundary=300000):
    if not known_primes:
        known_primes = [2]

    for number in range(max(known_primes), boundary+1):
        if all(number%prime != 0 for prime in known_primes):
            known_primes.append(number)
            yield number


if __name__ == '__main__':
    start = time.time()
    for prime in gen_primes():
        print(prime)
    print(time.time() - start)
