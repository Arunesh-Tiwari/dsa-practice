#User function Template for python3
import sys
sys.setrecursionlimit(5000)
class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0]*(W+1)
        
        for i in range(N):
            for j in range(W+1):
                cap = j 
                cv = val[i]
                cw = wt[i]
                
                if i==0:
                    dp[j] = (cap//cw)*cv
                else:
                    if cw<=cap:
                        dp[j] = max(cv+dp[cap-cw],dp[cap])
                    else:
                        dp[j] = dp[cap]
        return dp[W]
        
        


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