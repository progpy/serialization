import time
import sqlite3
from contextlib import closing


def gen_primes(c, known_primes=None, boundary=300000):
    if not known_primes:
        known_primes = [2]
        insert_prime(c, 2)

    yield from known_primes
    for number in range(max(known_primes), boundary+1):
        if all(number%prime != 0 for prime in known_primes):
            known_primes.append(number)
            insert_prime(c, number)
            yield number


def read_primes(c):
    return [row['prime'] for row in c.execute('SELECT prime FROM primes ORDER BY prime')]


def insert_prime(c, prime):
    c.execute('INSERT INTO primes(prime) VALUES (?)', [prime])


if __name__ == '__main__':
    start = time.time()
    conn = sqlite3.connect('primes.db', isolation_level=None)
    conn.row_factory = sqlite3.Row
    with closing(conn.cursor()) as c:
        c.execute('CREATE TABLE IF NOT EXISTS primes(prime INT)')

        known_primes = read_primes(c)
        for prime in gen_primes(c, known_primes):
            print(prime)
        print(time.time() - start)
