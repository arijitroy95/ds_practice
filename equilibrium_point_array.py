"""
Given an array A of n positive numbers. The task is to find the first Equilibrium Point in the array.
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Note: Return the index of Equilibrium point. (1-based index)

Example 1:

Input:
n = 5
A[] = {1,3,5,2,2}
Output: 3
Explanation: For second test case
equilibrium point is at position 3
as elements before it (1+3) =
elements after it (2+2).


Example 2:

Input:
n = 1
A[] = {1}
Output: 1
Explanation:
Since its the only element hence
its the only equilibrium point.


Your Task:
The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the
point of equilibrium. Return -1 if no such point exists.
"""


class Solution:
    def equilibriumPoint(self, array, n):
        total_array_sum = sum(array)
        equilibrium_point_idx = 0
        point_found = False
        sum_till_point = 0
        for i in range(n):
            if sum_till_point == total_array_sum - sum_till_point - array[i]:
                equilibrium_point_idx = i
                point_found = True
                break
            sum_till_point += array[i]
        if not point_found:
            return -1
        return equilibrium_point_idx + 1


print(Solution().equilibriumPoint([1], 1))
