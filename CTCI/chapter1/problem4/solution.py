"""
Palindrome Permutation

Given a string, write a function to check if it is a permutaion of a palindrome
a permutaion is a rearrangement of letters. the palindrome does not need to be 
limited to just dictionary words

input: tact toa
output true (permutation: 'taco cat' 'atco cta', etc)
"""
from collections import Counter

tests = {
    'tact toa': True
}

def palindrome_permutation_counts(s):
    """
    Go through and maintain counts of each letter, (not including spaces). If the length of s
    is even, then all counts of letter must be even, if the length is odd, then all counts 
    must be even except for one.
    """

    even = len(s) % 2 == 0
    c = Counter(s)
    if ' ' in c:
        del c[' ']

    if even:
        for l in c:
            if c[l] % 2 == 1:
                return False
        return True
    else:
        num_odd = 0
        for l in c:
            if c[l] % 2 == 1:
                num_odd += 1
                if num_odd > 1:
                    return False
        return True

def palindrome_permutation_bitvector(s):
    # create array of letter counts
    vector = [0] * 256
    for letter in s:
        vector[ord(letter)] += 1
    
    if len(s) % 2 == 1:
        # odd
        num_odd = 0
        for num in vector:
            if num % 2 == 1:
                num_odd += 1
                if num_odd > 1:
                    return False
        return True
    else:
        # even
        for num in vector:
            if num % 2 == 1:
                return False
        return True

def main():
    for t in tests:
        assert(palindrome_permutation(t) == tests[t])

main()