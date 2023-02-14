import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-z0-9]', '', s.lower())
        if res == res[::-1]:
            return True
        else:
            return False