#User function Template for python3

class Solution:
    def maxSubarrayXOR (self, N, arr):
        ans = -2147483648     #Initialize result
  
    # Pick starting points of subarrays
        for i in range(N):
             
            
            curr_xor = 0
      
            
            for j in range(i,N):
             
                curr_xor = curr_xor ^ arr[j]
                ans = max(ans, curr_xor)
             
         
        return ans
        # code here 
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
    
        ob = Solution()
        print(ob.maxSubarrayXOR(N,arr))
        

# } Driver Code Ends
