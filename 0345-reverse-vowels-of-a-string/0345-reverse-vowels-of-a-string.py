class Solution:
    def reverseVowels(self, s: str) -> str:
        set_vowels = set("aeiouAEIOU")
        enumerate_vowels = enumerate(s)
        storevowels = [[], []]
        reversed_vowels = []
        for index, value in enumerate_vowels:
            # Check if the character is a vowel
            if value in set_vowels:
                #store it
                storevowels[0].append(value)
                #store the index
                storevowels[1].append(index)
        # Reverse the list of vowels
        reversed_vowels = storevowels[0][::-1]
        # Replace the vowels in the original string with the reversed vowels
        for i in range(len(reversed_vowels)):
            s = s[:storevowels[1][i]] + reversed_vowels[i] + s[storevowels[1][i] + 1:]
        return s