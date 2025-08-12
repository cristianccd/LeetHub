class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pepe = str(digits)
        pepe = pepe.replace(",","")
        pepe = pepe.replace("[","")
        pepe = pepe.replace("]","")
        pepe = pepe.replace(" ","")
        number = int(pepe)
        number += 1
        return list(map(int,str(number)))