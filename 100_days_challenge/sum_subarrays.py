# https://practice.geeksforgeeks.org/problems/sum-of-subarrays2229/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

class solution:
    def get_sum(self, arr):
        n = len(arr)
        m = 1000000007
        res = 0
        if n == 0:
            return 0
        for i in range(n):
            res += arr[i] * (i + 1) * (n - i)

        return res % m


ob = solution()
print(ob.get_sum([1, 2, 3]))
