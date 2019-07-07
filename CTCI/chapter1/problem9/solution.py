"""
String rotation
assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring

waterbottle is a rotaion of erbottlewat
"""

def isSubstring(s1, s2):
    return s2 in s1

def is_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        return isSubstring(s1 + s1, s2)

def main():
    

main()