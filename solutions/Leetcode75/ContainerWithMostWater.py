class Solution:
    def maxArea(self, height: List[int]) -> int:

        if(len(height) == 2):
            return min(height[0], height[1])
        first = 0
        last = len(height) - 1
        largest = 0
        while(first <= last):
            height1 = height[first]
            height2 = height[last]

            if(height1 > height2):
                newBig = (height2) * (last - first)
                last -= 1
            elif(height1 <= height2):
                newBig = (height1) * (last - first)
                first += 1
            if(newBig >= largest):
                largest = newBig
        
        return largest
