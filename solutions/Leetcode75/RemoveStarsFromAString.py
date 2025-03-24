class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        string = ""
        for char in s:
            if char == '*' and len(stack) != 0:
                stack.pop()
            elif char != '*':
                stack.append(char)
        if len(stack) == 0:
            return ""
        string = ''.join(stack)
        return string
