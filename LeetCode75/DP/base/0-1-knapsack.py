class Knapsack:
    def recursive_sol(self, wt, val, W, n):
        if n == 0 or W == 0:
            return 0
        elif wt[n - 1] <= W:
            return max(val[n - 1] + self.recursive_sol(wt, val, W - wt[n - 1], n - 1),
                       self.recursive_sol(wt, val, W, n - 1))
        elif wt[n - 1] > W:
            return self.recursive_sol(wt, val, W, n - 1)


ob = Knapsack()
print(ob.recursive_sol([1, 3, 4, 5], [1, 4, 5, 7], 7, 4))
