class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')
        result = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = abs(current_sum - target)

                if diff < closest:
                    closest = diff
                    result = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
