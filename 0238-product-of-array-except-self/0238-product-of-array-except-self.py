class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_res = []
        # Initialize the result list with 1 for the first element
        if len(nums) == 0:
            return [0]
        if len(nums) == 1:
            return [0]
        racc = [1]
        lacc = [1]
        for i in range(len(nums)):
            ptl = i
            ptr = len(nums) - i - 1
            if i == 0:
                lacc.append(nums[ptl])
                racc.append(nums[ptr])
            else:
                lacc.append(lacc[i] * nums[ptl])
                racc.append(racc[i] * nums[ptr])
                
        for i in range(len(nums)):
            arr_res.append(lacc[i] * racc[len(nums) - i - 1])

        return arr_res