class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            sep = f"{len(word)}#"
            string += sep
            string += word
        return string

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            num = int(num)
            i += 1
            words.append(s[i: i + num])
            i += num
        return words
        

                

