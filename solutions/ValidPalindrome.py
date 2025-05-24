class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(i for i in s if i.isalnum())
        string = string.lower()
        reversed_string = string[::-1]
        reversed_string = reversed_string.lower()
        print(reversed_string)
        print(string)
        if reversed_string == string:
            return True
        return False
