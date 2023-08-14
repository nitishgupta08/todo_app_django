def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def greet(name):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello!"


def main():
    print(greet("Alice"))
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Fibonacci sequence of length 10: {fibonacci(10)}")

    prime_numbers = [num for num in range(1, 101) if is_prime(num)]
    print("Prime numbers from 1 to 100:", prime_numbers)


if __name__ == "__main__":
    main()
