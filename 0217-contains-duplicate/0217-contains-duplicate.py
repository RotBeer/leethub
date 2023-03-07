class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_dict = {}
        for n in nums:
            if n_dict.get(n):
                return True
            n_dict[n] = True
        return False