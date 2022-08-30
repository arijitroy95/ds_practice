"""
Given an array Arr[] of N integers.
Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


Example 1:

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which
is a contiguous subarray.
Example 2:

Input:
N = 4
Arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1
of element (-1)

Your Task:
You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes Arr[]
and N as input parameters and returns the sum of subarray with maximum sum.
"""
from sys import maxsize


class Solution:
    def maxSubArraySum(self,arr, N):
        current_max = arr[0]
        max_over_all = arr[0]
        for i in range(1, N):
            current_max = max(arr[i], current_max + arr[i])
            max_over_all = max(current_max, max_over_all)
        return max_over_all


def max_subarray_print(arr, n):
    max_over_all = -maxsize - 1
    current_max = 0
    start = 0
    end = 0
    s = 0
    for i in range(n):
        current_max += arr[i]
        if max_over_all < current_max:
            max_over_all = current_max
            start = s
            end = i
        if current_max < 0:
            current_max = 0
            s = i + 1

    print("MAX SUM IS: ", max_over_all)
    print(f"ARRAY PARTITION IS {start} TO {end}")


