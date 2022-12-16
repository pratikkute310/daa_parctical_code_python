def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapsack(W, wt, val, n - 1)
    else:
        return max(
            val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1),
            knapsack(W, wt, val, n - 1),
        )

wt = [3,5,5,8,4]
val = [10,20,21,30,16]
W = 20
n = len(val)
print(knapsack(W, wt, val, n))