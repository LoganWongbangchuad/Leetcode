class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #first time spotting a two pointer poblem
        l, r = 0, len(s) - 1
        while l < r:
            leftChar = s[l]
            rightChar = s[r]
            s[l] = rightChar
            s[r] = leftChar
            l += 1
            r -= 1
