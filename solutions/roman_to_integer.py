'''
I=1
V=5
X=10
L=50
C=100
D=500
M=1000

When subtract:
I before V or X
X before L or C
C before D or M
'''
class Solution:
    def romanToInt(self, s: str) -> int:

        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        counter = 0
        reversed_string = s[::-1]

        reversed_string+= "*"
        for i in range(len(reversed_string)):
            if reversed_string[i] == 'M':
                counter+= Roman[reversed_string[i]]
                if reversed_string[i + 1] == 'C':
                    counter-= Roman[reversed_string[i + 1]] * 2
            if reversed_string[i] == 'D':
                counter+= Roman[reversed_string[i]]
                if reversed_string[i + 1] == 'C':
                    counter-= Roman[reversed_string[i + 1]] * 2
            if reversed_string[i] == 'C':
                counter+= Roman[reversed_string[i]]
                if reversed_string[i + 1] == 'X':
                    counter-= Roman[reversed_string[i + 1]] * 2
            if reversed_string[i] == 'L':
                counter+= Roman[reversed_string[i]]
                if reversed_string[i + 1] == 'X':
                    counter-= Roman[reversed_string[i + 1]] * 2
            if reversed_string[i] == 'X':
                counter+= Roman[reversed_string[i]]
                if reversed_string[i + 1] == 'I':
                    counter-= Roman[reversed_string[i + 1]] * 2
            if reversed_string[i] == 'V':
                counter+= Roman[reversed_string[i]]
                if reversed_string[i + 1] == 'I':
                    counter-= Roman[reversed_string[i + 1]] * 2
            if reversed_string[i] == 'I':
                counter+= Roman[reversed_string[i]]
            if reversed_string[i] == "*":
                break
        return counter
