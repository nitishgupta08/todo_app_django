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


x = {"a": 37, "b": 42, "c": 927}

x = 123456789.123456789e123456789

if very_long_variable_name is not None and very_long_variable_name.field > 0 or very_long_variable_name.is_debug:
    z = "hello " + "world"
else:
    world = "world"
    a = "hello {}".format(world)
    f = rf"hello {world}"
if this and that:
    y = "hello " "world"  # FIXME: https://github.com/psf/black/issues/26


class Foo(object):
    def f(self):
        return 37 * -2

    def g(self, x, y=42):
        return y


def f(a: List[int]):
    return 37 - a[42 - u : y**3]


def very_important_function(
    template: str,
    *variables,
    file: os.PathLike,
    debug: bool = False,
):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, "w") as f:
        ...


custom_formatting = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]

regular_formatting = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]


if __name__ == "__main__":
    print("black test")
    main()
    print("Hello world")
