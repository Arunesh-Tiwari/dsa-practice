class Solution:
    def minimizeResult(self, expression: str) -> str:
        plusIndex = expression.find("+")

        mn = int(expression[0:plusIndex]) + int(expression[plusIndex + 1:])
        ans  = "(" + expression + ")"

        for leftIndex in range(0, plusIndex):
            for rightIndex in range(plusIndex + 1, len(expression)):
                midVal = int(expression[leftIndex: plusIndex]) + int(expression[plusIndex + 1: rightIndex + 1])
                leftVal = int(expression[0: leftIndex]) if leftIndex > 0 else 1
                rightVal = int(expression[rightIndex+1:]) if rightIndex + 1 < len(expression) else 1
                if leftVal * midVal * rightVal < mn:
                    mn = leftVal * midVal * rightVal
                    ans = expression[0:leftIndex] + "(" + expression[leftIndex: rightIndex + 1] + ")" + expression[rightIndex+1: ]
        return ans