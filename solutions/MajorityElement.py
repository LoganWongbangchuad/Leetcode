class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

        '''
        Initialize candidate as None
Initialize count as 0

For each element num in the array:
    If count is 0:
        Set candidate to num
    If num is equal to candidate:
        Increment count by 1
    Else:
        Decrement count by 1

Return candidate
        '''
