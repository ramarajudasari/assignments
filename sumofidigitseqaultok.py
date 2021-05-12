def subarraySum(nums,k):
        count = 0
        sum =[]
        sum.append(0)
        for i in range(1,len(nums)+1):
            sum.append(sum[i-1]+nums[i-1])

        for m in range(0,len(sum)):
            for n in range(m+1,len(sum)):
                if sum[n]-sum[m]==k:
                    count+=1
        return count
print(subarraySum([5,2,2,3,4,5],5))
