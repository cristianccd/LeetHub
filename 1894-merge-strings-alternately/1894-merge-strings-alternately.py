class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        n1 = len(word1)
        n2 = len(word2)
        if n1 >= n2:
            nmin = n2
        else:
            nmin = n1
        for i in range(nmin):
                word+=word1[i]
                word+=word2[i]
        if n1 >= n2:
            word+=word1[nmin:]
        else:
            word+=word2[nmin:]
        return word

        