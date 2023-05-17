#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
		SUM = sum(arr)
		dp = {}
		def solve(n,p1,SUM):
		    p2 = SUM-p1
		    if n==0:
		        return p1-p2
		    elif (n,p1) in dp:
		        return dp[(n,p1)]
		    else:
		        item = arr[n-1]
		        if p1-item>=p2+item:
		            c1 = solve(n-1, p1-item, SUM)
		            c2 = solve(n-1,p1,SUM)
		            c = min(c1,c2)
		        else:
		            c = solve(n-1,p1,SUM)
		        dp[n,p1] = c
		        return c
        return solve(N,SUM,SUM)
		            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends