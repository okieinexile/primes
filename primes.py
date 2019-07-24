#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 08:51:32 2019

@author: bobby
"""

from array import array
from itertools import count


def prime_generator() -> int:
    """
    This generates a list of primes.
    """
    
    #Start with the first prime.
    counter = count(2)
    candidate = next(counter)
    cache: list = [candidate]
    yield candidate
    
    # Set a flag.
    divisible = False
    while True:
        candidate = next(counter)
        # Check if the candidate is prime.
        for number in cache:
            # If number is greater than the squareroot of candidate, we are done.
            if number * number > candidate:
                break
            # If number divides candidate, candidate is not prime.
            if candidate % number == 0:
                divisible = True
                break
        # If is is prime, add it to the list.
        if not divisible:
            cache.append(candidate)
            yield candidate
        # Reset the flag.
        divisible = False
        
def primes(max_number_of_primes) -> iter:
    """This will give a finite list of primes."""
    number_primes = count(1)
    prime = prime_generator()
    while next(number_primes) <= max_number_of_primes:
        yield next(prime)
        
    
            
def prime_array(number_of_primes) -> array:
    """This will create an array of primes."""
    p = array('i',list(primes(number_of_primes)))
    return p

def save_prime_array(number_of_primes) -> None:
    """This will save an array of primes."""
    p = prime_array(number_of_primes)
    with open(f'prime{number_of_primes}.bin', 'wb') as prime_file:
        p.tofile(prime_file)
        
    return None

def get_prime_array(number_of_primes) -> array:
    """This will load primes into an array from a file."""
    p = array('i')
    with open(f'prime{number_of_primes}.bin', 'rb') as prime_file:
        p.fromfile(prime_file, number_of_primes)       
    return p
                