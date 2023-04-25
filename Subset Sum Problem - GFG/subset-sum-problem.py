#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here
        dp = {}
        def solve(n,cap):
            if cap==0:
                return 1
            elif n==0:
                return 0
            elif (n,cap) in dp:
                return dp[(n,cap)]
            else:
                if arr[n-1]<=cap:
                    ans = solve(n-1,cap-arr[n-1]) or solve(n-1,cap)
                else:
                    ans = solve(n-1,cap)
            dp[(n,cap)] = ans
            return ans
            
        return solve(N,sum)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends