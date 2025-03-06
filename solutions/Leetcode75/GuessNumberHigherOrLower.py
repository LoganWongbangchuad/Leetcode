# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #initialize first and last
        if(guess(n)==0):
            return n
        if(n==1):
            return 1
        elif(n == 2):
            if(guess(1)==0):
                return 1
            else:
                return 2
        else:

            first, last= 1,n
            number = n//2
            while guess(number) != 0:
                if(guess(number)==-1):
                    last=number
                    number = last // 2
                elif(guess(number)==1):
                    first = number
                    number = first + ((last - first)//2)
            return number
