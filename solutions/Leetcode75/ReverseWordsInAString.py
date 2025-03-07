class Solution:
    def reverseWords(self, s: str) -> str:
        stringArray=[]
        wordArray=[]
        word = ""
        for letter in s:
            if(letter != ' '):
                word += letter
            elif(letter == ' '):
                wordArray.append(word)
                word = ""
        wordArray.append(word)

        for spaces in wordArray:
            if(spaces==''):
                continue
            else:
                stringArray.append(spaces)

        string = ""
        for i in range(len(stringArray) - 1, -1, -1):
            if(i == 0):
                string += stringArray[i]
            else:
                string += stringArray[i] + " "
        
        return string
