"""
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.
In case of multiple subarrays, return the subarray which comes first on moving from left to right.
Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.
Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements
from 1st position to 5th position
is 15.


Your Task:
The task is to complete the function subarraySum() which takes arr, N and S as input parameters and returns an arraylist
 containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S.
 The two indexes in the array should be according to 1-based indexing.
 If no such subarray is found, return an array consisting only one element that is -1.
"""


class Solution:
    def subArraySum(self, arr, n, s):
        start_point = 0
        end_point = 0
        found = False
        total = 0
        if s == 0:
            return [-1]
        for i in range(n):
            total += arr[i]
            while total > s:
                total -= arr[start_point]
                start_point += 1
            if total == s:
                end_point = i
                found = True
                break
        if not found:
            return [-1]
        return start_point + 1, end_point + 1


print(Solution().subArraySum([2, 1], 4, 0))
