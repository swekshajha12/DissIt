def max_elements_sum_to_target_recursive(nums, target, n):
    if target == 0 or n == 0:
        return 0

    # If the last element is greater than the target, ignore it
    if nums[n - 1] > target:
        return max_elements_sum_to_target_recursive(nums, target, n - 1)

    # Either include or exclude the last element in the sum
    include_last = 1 + max_elements_sum_to_target_recursive(nums, target - nums[n - 1], n - 1)
    exclude_last = max_elements_sum_to_target_recursive(nums, target, n - 1)

    return max(include_last, exclude_last)


def max_elements_sum_to_target(nums, target):
    n = len(nums)
    dp = [0] * (target + 1)

    for i in range(1, n + 1):
        for j in range(target, nums[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j - nums[i - 1]] + 1)

    return dp[target]


print(max_elements_sum_to_target_recursive([1, 2, 3, 5, 1, 1, 1, 1], 5, 8))
print(max_elements_sum_to_target([10, 2, 3, 5, 1, 1, 1, 1], 5))
