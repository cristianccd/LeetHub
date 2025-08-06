class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        pos = len(s)-1
        sc = s[pos]
        #add I
        while sc == 'I' and pos >= 0:
            sum += 1
            pos -= 1   
            sc = s[pos] 
        while sc == 'V':
            sum += 5
            pos -= 1
            if pos < 0:
                return sum
            sc = s[pos]
            while sc == 'I' and pos >= 0:
                sum -= 1
                pos -= 1
                if pos >= 0:
                    sc = s[pos]
                else:
                    return sum   
        while sc == 'X':
            sum += 10
            pos -= 1
            if pos < 0:
                return sum
            sc = s[pos]
            while sc == 'I' and pos >= 0:
                sum -= 1
                pos -= 1
                if pos >= 0:
                    sc = s[pos]
                else:
                    return sum   
        while sc == 'L':
            sum += 50
            pos -= 1
            if pos < 0:
                return sum
            sc = s[pos]
            while sc == 'X' and pos >= 0:
                sum -= 10
                pos -= 1
                if pos >= 0:
                    sc = s[pos]
                else:
                    return sum   
        while sc == 'C':
            sum += 100
            pos -= 1
            if pos < 0:
                return sum
            sc = s[pos]
            while sc == 'X' and pos >= 0:
                sum -= 10
                pos -= 1
                if pos >= 0:
                    sc = s[pos]
                else:
                    return sum
        while sc == 'D':
            sum += 500
            pos -= 1
            if pos < 0:
                return sum
            sc = s[pos]
            while sc == 'C' and pos >= 0:
                sum -= 100
                pos -= 1
                if pos >= 0:
                    sc = s[pos]
                else:
                    return sum   
        while sc == 'M':
            sum += 1000
            pos -= 1
            if pos < 0:
                return sum
            sc = s[pos]
            while sc == 'C' and pos >= 0:
                sum -= 100
                pos -= 1
                if pos >= 0:
                    sc = s[pos]
                else:
                    return sum
        return sum