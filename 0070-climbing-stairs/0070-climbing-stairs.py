class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        pp, p = 1, 2
        for i in range(3, n):
            pp, p = p, pp+p
        return pp+p