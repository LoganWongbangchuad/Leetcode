class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maxAvg = total/k
        for i in range(len(nums)-k):
            total -= nums[i]
            total += nums[i+k]
            maxAvg = max(maxAvg, total/k)
        return maxAvg
        '''
        Solution that is wayyyy to slow
        counter=0
        maxAverage=0
        if(len(nums) == 0):
            return 0
        elif(len(nums)== 1):
            return nums[0]
        else:
            for i in range(len(nums)+1):
                if(i+k <= len(nums)):
                    l=0
                    while l < k:
                        counter+= nums[l+i]
                        l+=1
                        if(counter > maxAverage):
                            maxAverage = counter
                counter=0
            '''
