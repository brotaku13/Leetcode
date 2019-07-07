"""
One Away
There are three types of edits that can be performed on strings: insert a character, delete a character
or replace a character. Given two strings, determine if they are no more than one edit away. 

pale, ple true
pales, pale true
pale, bale true
pale, bake false
"""

def one_edit(s1, s2):
    # control flow
    if len(s1) == len(s2):
        # if they are equal in length, then we only need to check if we can replace at most one char
        return one_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        # if they are off by one in length, then we need to check if we can insert at most one character
        return one_insert(s1, s2):
    elif len(s1) - 1 == len(s2):
        # same here
        return one_insert(s2, s1):
    else:
        # else, their lengths differ too much and we should return false
        return False

def one_replace(s1, s2):
    found = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found:
                return False
            else:
                found = True
    return True

def one_insert(s1, s2):
    index1 = 0
    index2 = 0

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                # if the indexes are off and we found a difference, this means that we already found a difference previously
                # and need to return false
                return False
            # only move index2 since this belongs to the longer string
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    
    return True
