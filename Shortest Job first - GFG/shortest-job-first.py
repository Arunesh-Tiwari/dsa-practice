#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import math
class Solution:
    def solve(self, bt):
        # Code here
        # Sort burst times in ascending order
        bt.sort()
        
        total_wait_time = 0
        current_wait_time = 0
        
        for i in range(n):
            total_wait_time += current_wait_time
            current_wait_time += bt[i]
        
        # Calculate the average waiting time
        average_wait_time = total_wait_time // n
        
        return average_wait_time

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        bt = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(bt)
        print(res)
# } Driver Code Ends