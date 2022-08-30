"""
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

Example 1:

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.


Example 2:

Input:
N = 4, K = 3
arr[] = {5,6,8,9}
Output: 8 6 5 9


Your Task:
You don't need to read input or print anything. The task is to complete the function reverseInGroups() which takes the
array, N and K as input parameters and modifies the array in-place.
"""


class Solution:
    def reverseInGroups(self, arr: list, N: int, K: int):
        if K >= N:
            arr.reverse()
        else:
            for i in range(N // K + 1):
                if (i + 1) * K >= N:
                    b = arr[i * K:]
                else:
                    b = arr[i * K: (i + 1) * K]
                b.reverse()
                arr[i * K: (i + 1) * K] = b
        print(arr)


Solution().reverseInGroups([1,2,3,4], 4, 2)
