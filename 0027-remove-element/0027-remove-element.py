class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        cnt = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                cnt -= 1
            else:
                nums[idx] = nums[i]
                idx += 1

        return cnt