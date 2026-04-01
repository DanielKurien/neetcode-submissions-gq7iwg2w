from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res
    
    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        
        while i < len(s):
            # Find the length of the next string
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            # Extract the string of the specified length
            words.append(s[i:i + length])
            i += length
        
        return words
