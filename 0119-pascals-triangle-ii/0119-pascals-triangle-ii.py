from math import factorial as f

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [(f(rowIndex)) // (f(i) * f(rowIndex-i)) for i in range(rowIndex+1)]