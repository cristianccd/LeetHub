class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #shortest = min(str1, str2)
        #longest = max(str1, str2)
        #strreplace_min = ""
        #for i in range(len(shortest))[::-1]:
        #    strreplace = shortest[:i+1]
        #    if(longest.replace(strreplace, "") == ""):
        #        strreplace_min = strreplace
        #return strreplace_min
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]
        