class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while True:
            if n*n <= x:
                n += 1
            else:
                n -= 1
                break
        return n