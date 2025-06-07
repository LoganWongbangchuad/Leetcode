class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        my_list = list(set(nums))
        my_list.sort(reverse=True)
        print(my_list)
        if not my_list:
            return 0
        elif len(my_list) == 1:
            return my_list[0]
        elif len(my_list) == 2:
            return my_list[0]
        else:

            return my_list[2]
