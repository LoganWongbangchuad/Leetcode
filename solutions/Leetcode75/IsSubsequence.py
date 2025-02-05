class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        Slow Approach
        i,j=0,0
        isSubCounter = 0
        if(len(s)==0):
            return True
        elif(len(s)==1):
            letter = s[0]
            if letter in t:
                return True
        else:
            while j != len(t):
                if(isSubCounter == len(s)):
                    break
                elif(i < len(s)):
                    if(s[i] == t[j]):
                        i+=1
                        j+=1
                        isSubCounter+=1
                    else:
                        j+=1
        return isSubCounter == len(s)
        '''
        #Quick Approach
        if len(s)==0:
            return True
        j=0
        n=len(s)
        for i in range(len(t)):
            if t[i] == s[j]:
                j+=1
            
            if j==n:
                return True
        return False
        #Note: for-loop is slightly faster than while loop
