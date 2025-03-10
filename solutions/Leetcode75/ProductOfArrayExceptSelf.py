class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #correct answer
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

        
        
        
        '''
        my answer in O(n) time, but uses division.

        zeros=nums.count(0)
        product = 1
        productArray = []
        for i in range(len(nums)):
            if(nums[i] == 0):
                continue
            else:
                product = product * nums[i]

        
        for i in range(len(nums)):
            if(zeros > 1):
                productArray.append(0)
            elif zeros == 1:
                if(nums[i] == 0):
                    productArray.append(product)
                else:
                    productArray.append(0)
            else:
                productArray.append(product // nums[i])
        return productArray
        '''
