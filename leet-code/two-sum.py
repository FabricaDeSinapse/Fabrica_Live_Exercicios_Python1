"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# nums -> int[]
# target -> int
# return indices of the two numbers such that they add up to target

"""
Example 1

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            num1 = nums[i]

            for j in range(len(nums)):
                if j == i:
                    continue

                num2 = nums[j]

                total = num1 + num2

                if total == target:
                    return [i, j]


# Tests

print(Solution().twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(Solution().twoSum([3, 2, 4], 6))  # [1, 2]
print(Solution().twoSum([3, 3], 6))  # [0, 1]
print(Solution().twoSum([3, 2, 3], 6))  # [0, 2]
