#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 08:51:32 2019

@author: bobby
"""

from array import array
from itertools import count


def prime_generator() -> int:
    counter = count(2)
    candidate = next(counter)
    cache: list = [candidate]
    yield candidate
    divisible = False
    while True:
        candidate = next(counter)
        for number in cache:
            if candidate % number == 0:
                divisible = True
                break
        if not divisible:
            cache.append(candidate)
            yield candidate
        divisible = False
        
def primes(max_number_of_primes) -> iter:
    number_primes = count(1)
    prime = prime_generator()
    while next(number_primes) <= max_number_of_primes:
        yield next(prime)
        
        
def print_primes(N):
    for p in primes(N):
        print(p)
            
def prime_array(number_of_primes) -> array:
    p = array('i',list(primes(number_of_primes)))
    return p

                