class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ""
        for c in s:
            if ord(c) >=  ord('a') and ord(c) <= ord('z'):
                s_clean += c
            
            elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
                s_clean += c
            
            elif ord(c) >= ord('0') and ord(c) <= ord('9'):
                s_clean += c
            
        leftPointer = 0
        rightPointer = len(s_clean) - 1

        while leftPointer < rightPointer:
            if s_clean[leftPointer].lower() != s_clean[rightPointer].lower():
                return False
            leftPointer += 1
            rightPointer -= 1

        return True

