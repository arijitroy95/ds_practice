"""
Given two arrays of integers A[] and B[] of size N and M, the task is to check if a pair of values
(one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.



Example 1:

Input: N = 6, M = 4
A[] = {4, 1, 2, 1, 1, 2}
B[] = (3, 6, 3, 3)
Output: 1
Explanation: Sum of elements in A[] = 11
Sum of elements in B[] = 15, To get same
sum from both arrays, we can swap following
values: 1 from A[] and 3 from B[]
Example 2:

Input: N = 4, M = 4
A[] = {5, 7, 4, 6}
B[] = {1, 2, 3, 8}
Output: 1
Explanation: We can swap 6 from array A[] and 2 from array B[]
"""


def find_swap_values(a, n, b, m):
    a.sort()
    b.sort()
    if sum(a) == sum(b):
        return 1
    i = 0
    j = 0
    target_value = (sum(a) - sum(b)) // 2
    while i < n and j < m:
        cur_dif = a[i] - b[j]
        if cur_dif == target_value and sum(a) - sum(b) == 2 * (a[i] - b[j]):
            return 1
        if cur_dif < target_value:
            i += 1
        else:
            j += 1
    return -1


with open("/home/arijit/Downloads/fileInput.txt", "r") as fp:
    inputs = fp.readlines()

n, m = list(map(int, inputs[0].strip().split()))
a = list(map(int, inputs[1].strip().split()))
b = list(map(int, inputs[2].strip().split()))
print(find_swap_values(a, n, b, m))
