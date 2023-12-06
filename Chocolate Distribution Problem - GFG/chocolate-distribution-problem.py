#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        temp=sorted(A)
        i=0
        j=M-1
        min1=float("inf")
        while j<N:
            if (temp[j]-temp[i])<min1:
                min1=temp[j]-temp[i]
            i+=1
            j+=1
        return min1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends