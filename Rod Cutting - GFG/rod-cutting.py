#User function Template for python3

class Solution:
    def cutRod(self, price, N):
        #code here
        dp = {}
        def solve(cl, rl):
            if cl==0 or rl==0:
                return 0
            elif (cl,rl) in dp:
                return dp[(cl,rl)]
            else:
                val = price[cl-1]
                if cl<=rl:
                    c1 = val+ solve(cl,rl-cl)
                    c2 = solve(cl-1,rl)
                    c = max(c1,c2)
                else:
                    c = solve(cl-1,rl)
                dp[(cl,rl)] = c
                return c
        return solve(N,N)
            


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