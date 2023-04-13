class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for number in pushed:
            stack.append(number)
            if number == popped[j]:
                while stack and popped[j]==stack[-1]:
                    j += 1
                    stack.pop()
        if stack:
            return False
        return True
                
        