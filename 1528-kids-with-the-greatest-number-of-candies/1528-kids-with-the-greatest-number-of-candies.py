class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Output = []
        for i in range(len(candies)):
            if candies[i] + extraCandies < max(candies):
                Output.append(False)
            else:
                Output.append(True)
        return Output