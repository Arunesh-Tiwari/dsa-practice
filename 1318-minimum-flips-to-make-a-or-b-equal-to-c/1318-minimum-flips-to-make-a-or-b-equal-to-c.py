class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while not a == b == c == 0:
            a, A = divmod(a,2)
            b, B = divmod(b,2)
            c, C = divmod(c,2)

            if   A == B == 1 and C == 0 : ans+= 2
            elif A == B == 0 and C == 1 : ans+= 1
            elif A != B      and C == 0 : ans+= 1
        return ans