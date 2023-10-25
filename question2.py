def check_sum(nums, target):
    nums.sort()

    quadruplets = set()

    for a in range(len(nums) - 3):
        for b in range(a + 1, len(nums) - 2):
            left = b + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[a] + nums[b] + nums[left] + nums[right]

                if current_sum == target:
                    quadruplets.add((nums[a], nums[b], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return list(quadruplets)

# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = check_sum(nums, target)
print(result)
