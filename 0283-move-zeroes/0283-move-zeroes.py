from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        out = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            else:
                out.append(nums[i])
        for i in range(zeroes):
            out.append(0)
        nums[:] = out
        return #out

        