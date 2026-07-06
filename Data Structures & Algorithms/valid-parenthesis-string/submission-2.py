class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        a = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                elif a:
                    a.pop()
                else:
                    return False
            else:
                a.append(i)
        
        while stack:
            if not a:
                return False
            if stack.pop() > a.pop():
                return False
        
        return True 
            

        