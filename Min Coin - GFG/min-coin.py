#User function Template for python3

class Solution:
	def MinCoin(self, nums, amount):
	    dp = {}
	    nums.sort(reverse=True)
	    def solve(n,cap):
	        if cap==0:
	            return 0
	        elif n==0:
	            return float('INF')
	        elif (n,cap) in dp:
	            return dp[(n,cap)]
	        else:
	            val = nums[n-1]
	            if val<=cap:
	                c1 = 1 + solve(n,cap-val)
	                c2 = solve(n-1,cap)
	                c = min(c1,c2)
	            else:
	                c = float('INF')
	            dp[(n,cap)] = c
	            return c
	    temp = solve(len(nums),amount)
	    if temp>=10**9+7:
	        return -1
	    else:
	        return temp
		# Code here
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, amount = input().split()
		n = int(n)
		amount = int(amount)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.MinCoin(nums, amount)
		print(ans)
# } Driver Code Ends