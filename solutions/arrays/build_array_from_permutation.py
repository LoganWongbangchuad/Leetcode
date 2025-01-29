class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        nums_length = len(nums)
        for i in range(nums_length):
            ans.append(nums[nums[i]])
        return ans
