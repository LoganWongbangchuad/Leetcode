class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        listOfList = []

        dict1 = {}
        dict2 = {}

        for nums in nums1:
            dict1[nums]=1

        for nums in nums2:
            dict2[nums]=1
        list1 = []
        list2 = []
        for nums in nums1:
            if nums not in dict2:
                list1.append(nums)
                dict2[nums]=1
            else:
                continue
        
        for nums in nums2:
            if nums not in dict1:
                list2.append(nums)
                dict1[nums]=1
            else:
                continue

        listOfList.append(list1)
        listOfList.append(list2)

        return listOfList

        
        
