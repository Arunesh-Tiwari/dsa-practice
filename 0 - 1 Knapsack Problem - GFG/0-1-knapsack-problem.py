#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp = {}
        def solve(n,cap):
            if n==0 or cap==0:
                return 0
            if (n,cap) in dp:
                return dp[(n,cap)]
            else:
                cw = wt[n-1]
                cv = val[n-1]
                
                if cw > cap:
                    ans =  solve(n-1,cap)
                    
                else:
                    x = cv+solve(n-1,cap-cw)
                    y = solve(n-1,cap)
                    ans =  max(x,y)
                dp[(n,cap)] = ans
                return ans
            
        return solve(n,W)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends