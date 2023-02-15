class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n_dict = {}
        for n in nums:
            if n_dict.get(n):
                n_dict.pop(n)
            else:
                n_dict[n] = 1
        return list(n_dict.keys())[0]