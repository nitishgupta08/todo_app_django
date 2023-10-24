import random
import math


def prime_sieve(n):
    """Returns a list of all primes less than or equal to n."""
    sieve = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def factorize(n):
    """Returns a list of the prime factors of n."""
    factors = []
    for prime in prime_sieve(n):
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    return factors


def is_prime(n):
    """Returns True if n is prime, False otherwise."""
    return n in prime_sieve(n)


def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Returns the least common multiple of a and b."""
    return a * b // gcd(a, b)


def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def catalan(n):
    """Returns the nth Catalan number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 1
    else:
        return sum(catalan(i) * catalan(n - i - 1) for i in range(n))


def binomial_coefficient(n, k):
    """Returns the binomial coefficient nCk."""
    if k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k) + binomial_coefficient(n - 1, k - 1)


def quicksort(array):
    """Sorts the given array in ascending order using the quicksort algorithm."""
    if len(array) <= 1:
        return array
    else:
        pivot = array[-1]
        less = [x for x in array[:-1] if x <= pivot]
        greater = [x for x in array[:-1] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def mergesort(array):
    """Sorts the given array in ascending order using the mergesort algorithm."""
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left = mergesort(array[:mid])
        right = mergesort(array[mid:])
        return merge(left, right)


def merge(left, right):
    """Merges two sorted arrays into a single sorted array."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def binary_search(array, target):
    """Returns the index of target in array, or -1 if target is not in array."""
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_max_subarray(array):
    """Returns the maximum subarray of the given array."""
    max_so_far = float("-inf")
    max_ending_here = 0
    for i in range(100):
        print("test 4")

print('test 4')