#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp = [[0]*(m+1) for _ in range(n+1)]
        ans = 0
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    dp[i][j]=0
                else:
                    if S1[i-1]==S2[j-1]:
                        dp[i][j]= 1+dp[i-1][j-1]
                    ans = max(ans,dp[i][j])
        return ans
                        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends