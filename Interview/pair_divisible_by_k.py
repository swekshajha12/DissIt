from collections import defaultdict


class Solution:
    def solutionBruteForce(self, a, k):
        res = []
        for i in range(len(a)):
            for j in range(len(a)):
                if j != i:
                    if (a[j] + a[i]) % k == 0:
                        res.append((a[i], a[j]))
        print(res)
        return len(res) // 2

    def solutionOptimised(self, a, k):
        res = 0
        rem_count_map = defaultdict(list)
        for i in range(len(a)):
            rem_count_map[a[i]%k].append(a[i])
        for i in range(len(a)):
            rem = a[i]%k
            if k-rem in rem_count_map.keys():
                if a[i] in rem_count_map[k-rem]:
                    res+=len(rem_count_map[k-rem])-1
                else:
                    res += len(rem_count_map[k - rem])
            if rem==0 and rem in rem_count_map.keys():
                if a[i] in rem_count_map[rem]:
                    res+=len(rem_count_map[rem])-1
                else:
                    res += len(rem_count_map[rem])

        return res//2


ob = Solution()
print(ob.solutionBruteForce([1, 2, 3, 4, 5], 3))
print(ob.solutionOptimised([1, 2, 3, 4, 5], 3))
print(ob.solutionOptimised([1, 3, 5, 7, 9], 2))
print(ob.solutionOptimised([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(ob.solutionBruteForce([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
