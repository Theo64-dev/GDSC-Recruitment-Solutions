"""Question 2: Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order."""

# Solution :

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

# Example 1:
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
print("Example 1: "+ str(check_sum(nums1, target1)))

#Example 2 :
nums2 = [2, 2, 2, 2, 2]
target2 = 8
print("Example 2: "+ str(check_sum(nums2,target2)))
