class Solution:
    def combinePairs(s1: str, s2:str) -> list[str]:
        max_pairs = len(s1)*len(s2)
        result = [None] * max_pairs
        index = 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                result[index] = s1[i]+s2[j]
                index += 1
        return result
    
    def letterCombinations(self, digits: str) -> list[str]:
        phone_map = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
        '': "",
        }
        
        result = ""
        if digits == "":
            return []
        if len(digits) == 1:
            return list(phone_map[digits])
        
        for i in digits:
            if result != "":
                result = Solution.combinePairs(result,phone_map[i])
            else:
                result = phone_map[i]
        return result
        

        