"""
Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K.
Decrease the height of the tower by K ( you can do this operation only if the height of the tower is greater than or equal to K)
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.
Note: It is compulsory to increase or decrease the height by K for each tower.


Example 1:

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as
{3, 3, 6, 8}. The difference between
the largest and the smallest is 8-3 = 5.
Example 2:

Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:
11
Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between
the largest and the smallest is 17-6 = 11.
"""


def find_min_diff(arr, n, k):
    arr.sort()
    temp_min = arr[0]
    temp_max = arr[n - 1]
    max_diff = temp_max - temp_min
    for i in range(1, n):
        if arr[i] < k:
            continue
        # for each element calculate min of global min + k and current val - k
        temp_min = min(arr[0] + k, arr[i] - k)
        # for each element calculate max of global max - k and current val + k
        temp_max = max(arr[i - 1] + k, arr[n - 1] - k)
        max_diff = min(max_diff, temp_max - temp_min)
    return max_diff


def main():
    arr = [3, 9, 12, 16, 20]
    k = 3
    n = 5
    print(find_min_diff(arr, n, k))


if __name__ == '__main__':
    main()
