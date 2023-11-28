class Solution:
    def max_of_min_in_sliding_window(self, arr, k):
        min_res = []
        n = len(arr)
        for i in range(n - k + 1):
            min_res.append(min(arr[i:i + k]))
        print(min_res)
        return max(min_res)


ob = Solution()
print(ob.max_of_min_in_sliding_window([2, 5, 6, 3, 9, 5, 10, 56, 25], 3))
