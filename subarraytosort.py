class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f=-1
        s=-1
        
        for n in range(0,len(nums)-1):
            if nums[n]>nums[n+1]:
                
                if f==-1:
                    f=n
                s=n
        
        if s==0:
            s=1
        else:
            if  s!=-1:
                s=(s-f)+1
        return s+1
                    
