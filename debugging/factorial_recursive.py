#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    This function uses recursion to compute the factorial of a given non-negative integer.
    The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.
    For example, factorial(4) is 4 * 3 * 2 * 1 = 24.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the integer n. If n is 0, the function returns 1 as per the definition of factorial.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the input value from the command line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
