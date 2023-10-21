#User function Template for python3

def Search(arr,n,k):
    #code here
    target = k
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the left half is not sorted, the right half must be sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1  # Element not found
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        print(Search(arr,n,k))

# } Driver Code Ends