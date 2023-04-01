class Solution:
    def isHappy(self, n: int) -> bool:
        val = set()
        while n != 1:
            t = 0
            while n != 0:
                t += (n%10)**2
                n //= 10
            if t in val:
                return False

            val.add(t)
            n = t
        return True