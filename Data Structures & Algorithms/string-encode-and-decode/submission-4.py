class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            length = len(word)
            string += f"{length}&{word}"
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        while i < len(s):
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            num = int(num_str)
            if i < len(s) and s[i] == '&':
                words.append(s[i + 1 : i + 1 + num])
                i = i + 1 + num
        return words