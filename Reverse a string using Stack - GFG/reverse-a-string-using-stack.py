#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    
    #Add code here
    stack = []
    
    # Push each character onto the stack
    for char in S:
        stack.append(char)
    
    # Pop characters from the stack to construct the reversed string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str
        

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends