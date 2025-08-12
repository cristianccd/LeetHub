class Solution:
    def mySqrt(self, x: int) -> int:
        hi = x
        lo = 0

        if x <= 1:
            return x

        while lo < hi:
            mid = (hi + lo) // 2
            #found
            if int(mid * mid) == x or mid == lo or mid == hi:
                return mid
            #update hi
            elif int(mid * mid) > x:
                hi = mid
            #update lo
            else:
                lo = mid
        