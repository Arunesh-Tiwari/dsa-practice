#User function Template for python3
import sys
sys.setrecursionlimit(5000)
class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        # dp = {}
        # def solve(n,cap):
        #     if n==0 or cap==0:
        #         return 0
        #     elif (n,cap) in dp:
        #         return dp[(n,cap)]
        #     else:
        #         cw = wt[n-1]
        #         cv = val[n-1]
        #         if cw<=cap:
        #             c1 = cv+solve(n,cap-cw)
        #             c2 = solve(n-1,cap)
        #             c = max(c1,c2)
        #         else:
        #             c = solve(n-1,cap)
        #         dp[(n,cap)] = c
        #         return c
        # return solve(N,W)
        
        dp = [[0]*(W+1) for _ in range(N)]
        
        for i in range(N):
            for j in range(W+1):
                cap = j
                cv = val[i]
                cw = wt[i]
                
                if i==0:
                    dp[i][j] = (cap//cw)*cv
                else:
                    if cw<= cap:
                        dp[i][j] = max(cv+dp[i][cap-cw],dp[i-1][cap])
                    else:
                        dp[i][j] = dp[i-1][cap]
        return dp[N-1][W]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends