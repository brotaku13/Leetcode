class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        elif haystack == '':
            return -1
        
        needle_index = 0
        len_needle = len(needle)
        
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[needle_index]:
                needle_index += 1
                if needle_index == len_needle:
                    return i - needle_index + 1
                
            elif needle_index > 0:
                i -= needle_index
                needle_index = 0
                
            i += 1
        
        return -1