from sys import stdin

def sieve_of_eratosthenes(n):
    n += 1 # Add one to check for primes up to and including n
    sqrt_n = int(n ** 0.5 + 1)

    potential_primes = [True] * n
    potential_primes[0] = potential_primes[1] = False

    # Integers up to and including int(sqrt(n)) have to be checked.
    # There exists a proof somewhere
    for i in range(2, sqrt_n):
        potential_prime = potential_primes[i]
        if potential_prime:
            # All non-primes betwen i and i ** 2 have allready been removed.
            # There exists a proof for this.
            for j in xrange(i ** 2, n, i):
                potential_primes[j] = False

    actual_primes = []
    for i, prime in enumerate(potential_primes):
        if prime:
            actual_primes.append(i)

    return actual_primes
