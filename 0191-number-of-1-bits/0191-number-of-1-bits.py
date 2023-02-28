class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while n != 0:
            output += 1 if n & 1 else 0
            n >>= 1
        return output