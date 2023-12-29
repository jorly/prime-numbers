"""
Author: Jorly Metzger, metzge30@purdue.edu
License: GPLv3
Date: 09/21/2023

Description:
    Program takes in a number and determines if it is prime
"""

"""Import modules."""
import math 

"""Classes and Functions."""

####
# Functions returns True if number is prime (False otherwise) using
# Sieve of Eratosthenesa algorithm
#
# number (input): number to evaluatie
# denominator: determines if the number can be divided by a second number (i.e., not prime)
#
# ##
def is_prime(n):
    if n <= 1: return False

    max = int(math.sqrt(n)) + 1
    primes = [True] * max
    primes[0] = primes[1] = False

    for i in range(2, max):
        for composite in range(i*i, max, i):
            primes[composite] = False

    for denominator in range(2, max):
        if primes[denominator] and (n % denominator == 0):
            return False

    return True

""" === MAIN === """

####
# number (input): number to evaluation
#
# ##
def main():
    while (True):
        number = int(input("Enter a positive integer (-1 to quit): "))
        if (number == -1): break
        if (is_prime(number)):
            print (f"  {number} is prime!")
        else:
            print (f"  {number} is not prime.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
