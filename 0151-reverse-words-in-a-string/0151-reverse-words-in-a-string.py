from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_words = s.split()
        st = " ".join(list_of_words[::-1])
        return st
        