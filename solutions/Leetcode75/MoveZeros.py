class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        long running time answer!!!
        if(len(nums)>1):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if(nums[i] != 0 and nums[j] != 0):
                        continue
                    elif(nums[i] == 0 and nums[j] != 0):
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
        """
        n = len(nums)
        j = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
