#User function Template for python3

class Solution:
    def cutRod(self, price, N):
        #code here
        dp = [[0]*(N+1) for _ in range(N+1)]
        
        for i in range(N+1):
            for j in range(N+1):
                cl = i
                rl = j
                if cl==0 or rl==0:
                    dp[i][j] = 0
                else:
                    val = price[cl-1]
                    if cl<=rl:
                        c1 = val+dp[cl][rl-cl]
                        c2 = dp[cl-1][rl]
                        dp[i][j] = max(c1,c2)
                    else:
                        dp[i][j] = dp[cl-1][rl]
        return dp[N][N]
        # dp = {}
        # def solve(cl, rl):
        #     if cl==0 or rl==0:
        #         return 0
        #     elif (cl,rl) in dp:
        #         return dp[(cl,rl)]
        #     else:
        #         val = price[cl-1]
        #         if cl<=rl:
        #             c1 = val+ solve(cl,rl-cl)
        #             c2 = solve(cl-1,rl)
        #             c = max(c1,c2)
        #         else:
        #             c = solve(cl-1,rl)
        #         dp[(cl,rl)] = c
        #         return c
        # return solve(N,N)
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends