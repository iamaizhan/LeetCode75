# Array / String
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "AEIOUaeiou"
        vowel_list = []
        for char in s:
            if char in vowels:
                vowel_list.append(char)
        result = []
        vowel_index = len(vowel_list) - 1
        
        for char in s:
            if char in vowels:
                result.append(vowel_list[vowel_index])
                vowel_index -= 1
            else:
                result.append(char)
        
        return "".join(result)
