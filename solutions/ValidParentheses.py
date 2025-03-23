class Solution:
    def isValid(self, s: str) -> bool:
        #fast solution altough both solutions are technically O(n)
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack





        '''
        My slow solution
        dict = {'(':')', '{':'}', '[':']'}
        stack = []
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        if len(s) < 2:
            return False
        for letter in s:
            if letter == '(' or letter == '{' or letter == '[':
                stack.append(letter)
                #print(stack)
            elif (letter == ')' or letter == '}' or letter == ']') and len(stack) != 0:
                top = stack.pop()
                if dict[top] == letter:
                    continue
                else:
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        return True
        '''
