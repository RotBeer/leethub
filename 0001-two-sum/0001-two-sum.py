class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort(reverse=True)
        for idx1, item1 in enumerate(nums):
            for idx2, item2 in enumerate(nums):
                if item1 + item2 == target and idx1 != idx2:
                    return [idx1, idx2]