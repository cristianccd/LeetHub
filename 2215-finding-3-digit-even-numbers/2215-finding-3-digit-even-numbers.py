class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from typing import List
        
        nums = set()
        n = len(digits)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    
                    if digits[i] == 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num % 2 == 0:
                        nums.add(num)

        return sorted(nums)
