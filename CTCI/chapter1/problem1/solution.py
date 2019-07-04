#is_unique will determine if a string has all unique characters. What if you cannot use any additional
#data structures
from collections import Counter

tests = {
    'asdf': True,
    'Brian': True,
    '': True,
    'aa': False,
    'asdf asdfasdf': False
}

def is_unique_hashmap(string):
    c = Counter(string)
    for letter in c:
        if c[letter] > 1:
            return False
    return True

def is_unique_bitvector(string):
    letters = 0
    for l in string:
        if (1 << ord(l) & letters) > 0:
            return False
        else:
            letters = letters | 1 << ord(l)
    return True

def main():
    test_func = is_unique_bitvector

    for test in tests:
        assert(test_func(test) == tests[test])

main()