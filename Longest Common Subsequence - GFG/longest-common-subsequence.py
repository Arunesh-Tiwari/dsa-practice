#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,str1,str2):
        dp = [[0]*(y+1) for _ in range(x+1)]
        
        for i in range(x+1):
            for j in range(y+1):
                m = i
                n = j
                if m==0 or n==0:
                    dp[i][j] = 0
                else:
                    if str1[m-1]==str2[n-1]:
                        dp[i][j] = 1+dp[m-1][n-1]
                    else:
                        c1 = dp[m-1][n]
                        c2 = dp[m][n-1]
                        dp[i][j] = max(c1,c2)
        return dp[x][y]
        
        # code here
        # dp = {}
        # def solve(s1,s2,m,n):
        #     if m==0 or n==0:
        #         return 0
        #     elif (m,n) in dp:
        #         return dp[(m,n)]
        #     else:
        #         if s1[m-1]==s2[n-1]:
        #             c = 1+solve(s1,s2,m-1,n-1)
        #         else:
        #             c1 = solve(s1,s2,m-1,n)
        #             c2 = solve(s1,s2,m,n-1)
        #             c = max(c1,c2)
        #         dp[(m,n)] = c
        #         return c
        # return solve(str1,str2,x,y)


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
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends