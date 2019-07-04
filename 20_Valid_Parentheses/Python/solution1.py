class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        
        p = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        
        stack = []
        close_p = p.keys()
        open_p = p.values()
        
        for letter in s:
            if letter in open_p:
                # must deal with opening parentheses
                stack.append(letter)
                
            elif letter in close_p:
                # must deal with close parentheses
                if len(stack) == 0:
                    return False
                
                elif stack[-1] != p[letter]:
                    return False
                
                else:
                    stack.pop()
                
            else:
                # not in either
                return False
        
        if len(stack) == 0:
            return True
        return False