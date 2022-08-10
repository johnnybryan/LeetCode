class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'(':')', '[':']', '{':'}'}
        stack = []
        for char in s:
            if char in parens:
                stack.append(char)
            elif len(stack) is 0 or parens[stack.pop()] != char:
                return False
        return len(stack) == 0
            
                
                
    