class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        s = list(s)
        count = 0
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')' and len(stack) != 0:
                if stack[-1] == '(':
                    stack.pop(-1)
            else:
                count += 1
        return count + len(stack)


        