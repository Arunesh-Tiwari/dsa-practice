import sys
sys.setrecursionlimit(10**6)
class Solution:
    def solver(self, n, lst):
        if n <= 0:
            lst.append(n)
            return
        lst.append(n)
        self.solver(n-5,lst)
        lst.append(n)
            
    
    def pattern(self, N):
        lst = []
        if N <= 0:
            return [N]
        self.solver(N,lst)
        return lst

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends