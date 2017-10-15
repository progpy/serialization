import os
import time

SAVE_NAME = 'primes.txt'
TEMP_NAME = 'primes.tmp.txt'


def gen_primes(known_primes=None, boundary=300000):
    if not known_primes:
        known_primes = [2]

    yield from known_primes
    for number in range(known_primes[-1], boundary+1):
        if all(number%prime != 0 for prime in known_primes):
            known_primes.append(number)
            yield number
        if number % 1000 == 0:
            save_primes(known_primes)


def save_primes(known_primes):
    with open(TEMP_NAME, 'wt') as f:
        for prime in known_primes:
            f.write('{}\n'.format(prime))
    os.rename(TEMP_NAME, SAVE_NAME)


def read_primes():
    primes = []
    try:
        with open(SAVE_NAME, 'rt') as f:
            primes = [int(line) for line in f]
    except IOError:
        pass
    return primes

if __name__ == '__main__':
    start_time = time.time()
    known_primes = read_primes()
    for prime in gen_primes(known_primes):
        print(prime)
    print(time.time() - start_time)
