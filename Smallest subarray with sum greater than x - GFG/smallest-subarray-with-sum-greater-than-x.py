import math

class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here
        if n == 1:
            if a[0] > x:
                return 1
            return 0
        
        ans = math.inf
        sm_yet = a[0]
        i, j = 0, 1
        while i < n and j < n and i <= j:
            if i == j and a[i] > x:
                return 1
            if a[j] + sm_yet > x:
                ans = min(ans, j-i+1)
                sm_yet -= a[i]
                i += 1
            else:
                sm_yet += a[j]
                j += 1
                
        return ans if math.isfinite(ans) else 0
            
        



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends