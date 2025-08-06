class Solution:
    def compress(self, chars: List[str]) -> int:
        newchar = []
        count = 1
        j = 0
        if len(chars) == 0:
            return 0
        if len(chars) == 1:
            return 1

        for i in range(len(chars)-1):
            if i == j:
                for j in range(i + 1,len(chars)):
                    if chars[i] == chars[j]:
                        count += 1
                    else:
                        break
                newchar.append(str(chars[i]))
                if count > 1 and count < 10:
                    newchar.append(str(count))
                elif count > 9:
                    #split into multiple characters
                    for digit in str(count):
                        newchar.append(str(digit))
                count = 1
        if chars[len(chars)-1] != chars[len(chars)-2]:
            newchar.append(str(chars[len(chars)-1]))
        
        
        chars[:] = newchar
        l = len(chars)
        return l