class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            #left edge case
            if i == len (flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
                break
            #middle case
            if i > 0 and i < len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            #right edge case
            if i == 0 and flowerbed[i] == 0 and (i + 1) < len(flowerbed) and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
        else:
            return False
        