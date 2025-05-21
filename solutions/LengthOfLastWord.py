class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stringList = s.split()
        return len(stringList[len(stringList) - 1])
