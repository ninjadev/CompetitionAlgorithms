from sieve_of_eratosthenes import sieve_of_eratosthenes

primes_to_20 = [2, 3, 5, 7, 11, 13, 17, 19]
sieve_20 = sieve_of_eratosthenes(20)

print "(Got ", sieve_20, ")"
if sieve_20 == primes_to_20:
  print "[PASS] Sieve 20 test pass\n"
else:
  print "[FAIL] Sieve 20 test fail\n"

primes_to_3 = [2,3]
sieve_3 = sieve_of_eratosthenes(3)

print "(Got ", sieve_3, ")"
if sieve_3 == primes_to_3:
  print "[PASS] Sieve 3 test pass\n"
else:
  print "[FAIL] Sieve 3 test fail\n"
