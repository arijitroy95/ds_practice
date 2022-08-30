"""
Given weights and values of N items, we need to put these items in a knapsack of capacity W
to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item.



Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack.
Example 2:

Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output:
160.00
Explanation:
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.
"""


class Item:
    def __init__(self, weight, value):
        self.value = value
        self.weight = weight


def fractional_knapsack(w, items, n):
    items.sort(key=lambda x: (x.value / x.weight), reverse=True)
    if n == 0 or w == 0:
        return 0
    max_value = 0
    for i in items:
        if i.weight <= w:
            max_value += i.value
            w -= i.weight
        else:
            max_value += ((w / i.weight) * i.value)
            break
    return max_value


vals = [60, 100, 120]
weights = [10, 20, 30]
N = 3
W = 50
print(fractional_knapsack(W, [Item(weights[i], vals[i]) for i in range(N)], N))


