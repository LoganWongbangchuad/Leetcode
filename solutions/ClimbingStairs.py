class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            prev = 1
            curr = 2

            for i in range(2, n):
                next = prev + curr
                prev = curr
                curr = next

            return curr




'''
recursive solution
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
'''

