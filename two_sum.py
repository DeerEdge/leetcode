class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n1_ind in range(len(nums) - 1):
            for n2_ind in range(len(nums) - 1):
                if n2_ind != n1_ind and nums[n1_ind] + nums[n2_ind] == target:
                    return [n1_ind, n2_ind]
