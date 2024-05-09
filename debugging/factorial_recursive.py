#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given number using recursion.

    Parameters:
    - n (int): The number for which factorial is to be calculated.

    Returns:
    - int: The factorial of the given number.
    """
    if n == 0:  # If the number is 0, factorial is 1
        return 1
    else:
        # Recursive call to calculate factorial
        return n * factorial(n-1)

# Main code
if __name__ == "__main__":
    # Extract the number from command-line argument
    number = int(sys.argv[1])
    # Calculate factorial and print the result
    result = factorial(number)
    print(result)
