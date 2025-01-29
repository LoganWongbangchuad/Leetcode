class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for ops in operations:
            if ops[0] == '+':
                x = x + 1
            elif ops[0] == '-':
                x = x - 1
            else:
                if ops[1] == '+':
                    x = x + 1
                elif ops[1] == '-':
                    x = x - 1
        return x
