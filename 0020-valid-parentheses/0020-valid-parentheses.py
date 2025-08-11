class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in pairs.values():          # opening
                stack.append(ch)
            elif ch in pairs:                 # closing
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                return False                  # invalid character
        return not stack                      # all opened were closed
        