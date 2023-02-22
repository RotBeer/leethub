class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        for i, x in enumerate(columnTitle[::-1]):
            output += 26**i * (ord(x) - ord('A') + 1)
        return output