"""
Given an array Arr (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion.
The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in the output
i.e you have to iterate on the original array only.

Example 1:

Input:
N = 7
take i, i+1, i+2 and arrange it
Arr[] = {4, 3, 7, 8, 6, 2, 1} i=0 biggest in middle
===> 3 7 4 8 6 2 1, i=1 smallest in middle
===> 3 7 4 8 6 2 1, i=2 biggest in middle
===> 3 7 4 8 6 2 1, i=3 smallest in middle
===> 3 7 4 8 2 6 1, i=4 biggest in middle
===> 3 7 4 8 2 6 1, reached till end
Output: 3 7 4 8 2 6 1
Explanation: 3 < 7 > 4 < 8 > 2 < 6 > 1
Example 2:

Input:
N = 4
Arr[] = {1, 4, 3, 2}
Output: 1 4 2 3
Explanation: 1 < 4 > 2 < 3
Your Task:
You don't need to read input or print anything. Your task is to complete the function zigZag() which takes the array of
integers arr and n as parameters and returns void. You need to modify the array itself.
"""


class Solution:
    @staticmethod
    def arrange_3_ele(eles, max_in_mid=True):
        if max_in_mid:
            if eles[1] < eles[0]:
                eles[0], eles[1] = eles[1], eles[0]
            if eles[1] < eles[2]:
                eles[1], eles[2] = eles[2], eles[1]
        else:
            if eles[1] > eles[0]:
                eles[0], eles[1] = eles[1], eles[0]
            if eles[1] > eles[2]:
                eles[1], eles[2] = eles[2], eles[1]

    def zigZag(self, arr, n):
        if n == 2:
            if arr[0] > arr[1]:
                arr.reverse()
        elif n == 3:
            self.arrange_3_ele(arr)
        else:
            for i in range(n - 2):
                max_in_mid = False
                if i % 2 == 0:
                    max_in_mid = True
                temp_section = arr[i: i + 3]
                self.arrange_3_ele(eles=temp_section, max_in_mid=max_in_mid)
                arr[i: i + 3] = temp_section
        print(arr)


Solution().zigZag([4, 3, 7, 8, 6, 2, 1], 7)
