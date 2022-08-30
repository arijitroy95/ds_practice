"""
Given an array, rotate the array by one position in clock-wise direction.


Example 1:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4


Example 2:

Input:
N = 8
A[] = {9, 8, 7, 6, 4, 2, 1, 3}
Output:
3 9 8 7 6 4 2 1
"""


def rotate(arr, n):
    if n <= 1:
        return
    prev_next_value = 0
    for i in range(n):
        if i < n - 1:
            current_next_val = arr[i + 1]
        else:
            current_next_val = 0
        if i == 0:
            arr[i + 1] = arr[i]
        elif i < n - 1:
            arr[i + 1] = prev_next_value
        else:
            arr[0] = prev_next_value
        prev_next_value = current_next_val


rotate([9, 8, 7, 6, 4, 2, 1, 3], 8)
