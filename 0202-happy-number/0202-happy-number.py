class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}
        while n != 1:
            sum_s = 0
            while n != 0:
                n, s = divmod(n, 10)
                sum_s += s**2
            if visited.get(sum_s):
                return False
            visited[sum_s] = True
            n = sum_s
        return True
