#User function Template for python3

class Solution:
    def middle(self,A,B,C):
        #code here
        if A < B:
        # A is smaller
            if B < C:
                # A < B < C, so B is the middle number
                return B
            elif A < C:
                # A < C < B, so C is the middle number
                return C
            else:
                # C < A < B, so A is the middle number
                return A
        else:
            # B is smaller
            if A < C:
                # B < A < C, so A is the middle number
                return A
            elif B < C:
                # B < C < A, so C is the middle number
                return C
            else:
                # C < B < A, so B is the middle number
                return B



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends