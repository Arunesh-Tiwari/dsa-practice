#User function Template for python3
import sys
sys.setrecursionlimit(5000)
class Solution:
    def count(self, coins, N, SUM):
        dp = {}
        def solve(n,cap):
            if cap==0:
                return 1
            elif n==0:
                return 0
            elif (n,cap) in dp:
                return dp[(n,cap)]
            else:
                val = coins[n-1]
                if val<=cap:
                    c1 = solve(n,cap-val)
                    c2 = solve(n-1,cap)
                    c = c1+c2 
                else:
                    c = solve(n-1,cap)
                dp[(n,cap)] = c 
                return c
        return solve(N,SUM)
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends