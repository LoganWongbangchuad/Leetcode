class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict={}

        for num in arr:
            dict[num] = 0
        for num in arr:
            dict[num] = dict[num] + 1

        keys = list(dict.keys())
        for i, key in enumerate(keys):
            occur= dict[key]
            for key2 in keys[i+1:]:
                if(occur == dict[key2]):
                    return False
        return True
        print(dict)
