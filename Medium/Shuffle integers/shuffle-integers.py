class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        ctr = 1
        ptr = n//2
        for i in range(n//2):
            arr.insert(ctr,arr.pop(ptr))
            ptr+=1
            # print(arr)
            ctr+=2


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends