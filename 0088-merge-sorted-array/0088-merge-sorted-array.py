class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #check until nums 1 is 0
        if m <= 1 and n == 0:
            return
        if m == 0 and n >= 1:
            nums1[:] = nums2
            return
        
        i = 0
        j = 0
        result = []
        #check until nums 1 is 0
        while i+j < m+n:
            #check which is biggest
            #in case that j is over bounds
            if j >= n:
                result.append(nums1[i])
                i+=1
            #if nums1 is smaller than 2, leave as is and increment i
            elif nums1[i] < nums2[j]:
                #could be a 0
                if i >= m:
                    result.append(nums2[j])
                    j += 1
                else:
                    result.append(nums1[i])
                    i += 1
            #if nums1 is bigger than 2, insert 2 and increment j
            elif nums1[i] >= nums2[j]:
                result.append(nums2[j])
                j += 1

        nums1[:] = result        
        