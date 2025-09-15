# recursive_functions.py

# Function 1: Calculate sum of numbers from 0 to n using recursion
def sum_recursive(total, i, n):
    """
    Sums numbers from i to n recursively.
    :param total: Accumulator for the sum
    :param i: Current number
    :param n: Final number to sum up to
    """
    if i > n:
        print(f"Sum from 0 to {n} is: {total}")
        return
    sum_recursive(total + i, i + 1, n)


# Function 2: Sum of first n natural numbers using recursion
def sum_natural(n):
    """
    Returns sum of first n natural numbers using recursion.
    :param n: The number up to which sum is calculated
    :return: Sum from 1 to n
    """
    if n == 1:
        return 1
    return n + sum_natural(n - 1)


# Function 3: Calculate factorial of n using recursion
def factorial(n):
    """
    Returns factorial of n using recursion.
    :param n: The number to calculate factorial of
    :return: n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


# Driver code
if __name__ == "__main__":
    print("=== Recursive Sum from 0 to 10 ===")
    sum_recursive(0, 0, 10)   # Output: 55

    print("\n=== Sum of first 4 natural numbers ===")
    print(sum_natural(4))     # Output: 10

    print("\n=== Factorial of 4 ===")
    print(factorial(4))       # Output: 24
