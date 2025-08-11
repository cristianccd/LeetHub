class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #start from the middle
        #is the low part smaller, then the lower part is sorted
     #start from the middle
    #is the low part smaller, then the lower part is sorted
        high = len(nums) - 1
        low = 0
        
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        #while not sorted, continue
        while low <= high:
            mid = (low + high) // 2
            #found
            if nums[mid] == target:
                return mid
            #sorted left
            if nums[low] <= nums[mid]:
                #target is on the left
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                #target is on the right
                else:
                    low = mid + 1
            #sorted right
            else:
                #target is between low and mid, not sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1