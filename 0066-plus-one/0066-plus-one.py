class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = 0
        while True:
            idx += 1
            if idx > len(digits):
                digits = [0] + digits
            digits[-idx] += 1
            if digits[-idx] < 10:
                return digits
            else:
                digits[-idx] = 0