class Solution:
    def duplicates(self, arr, N):
        ans = []
    
        for i in range(N):
            index = arr[i] % N
            arr[index] += N
    
        for i in range(N):
            if (arr[i] // N) > 1:
                ans.append(i)
    
        if len(ans) == 0:
            return [-1]
        else:
            return ans


    	    
    	    
    	    
    	
    	    
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends