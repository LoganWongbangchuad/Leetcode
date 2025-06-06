class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == k:
                counter +=1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return counter
