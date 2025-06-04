class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for stone in stones:
            if jewels.find(stone) != -1:
                counter += 1
            
        return counter
