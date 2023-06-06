class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        t = sorted(str(n))
        i = 0
        while len(str(2**i))<=len(str(n)):
            if t==sorted(str(2**i)):
                return True
            i+=1
        return False