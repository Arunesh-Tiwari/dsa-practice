class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		Intervals.sort()
		ans = []
		ans.append(Intervals[0])
		for i in range(len(Intervals)):
		  #  if not ans:
		  #      ans.append(Intervals[i])
		    if Intervals[i][0]<=ans[-1][1]:
		        ans[-1][1]=max(ans[-1][1], Intervals[i][1])
		    else:
		        ans.append(Intervals[i])
		return ans


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends