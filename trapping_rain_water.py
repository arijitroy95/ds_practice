"""
Given an array arr[] of N non-negative integers representing the height of blocks.
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.
Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10

Example 2:
Input:
N = 4
arr[] = {7,4,0,9}
Output:
10
Explanation:
Water trapped by above
block of height 4 is 3 units and above
block of height 0 is 7 units. So, the
total unit of water trapped is 10 units.
Example 3:

Input:
N = 3
arr[] = {6,9,9}
Output:
0
Explanation:
No water will be trapped.
"""


class Solution:
    def trappingWater_memo(self, arr, n):
        left_side_heights = [0] * n
        right_side_heights = [0] * n
        water = 0
        left_side_heights[0] = arr[0]
        for i in range(1, n):
            left_side_heights[i] = max(left_side_heights[i-1], arr[i])
        right_side_heights[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right_side_heights[i] = max(right_side_heights[i + 1], arr[i])
        for i in range(n):
            water += min(left_side_heights[i], right_side_heights[i]) - arr[i]
        return water

    def trapping_water_stack(self, arr, n):
        stack = []
        ans = 0
        for i in range(n):
            # pop from stack until stack is empty or current bar height is greater than stack top
            while stack and arr[stack[-1]] < arr[i]:
                top_height_idx = stack.pop()
                # if stack got empty get out
                if not stack:
                    break
                # calculate distance between left and right bar
                distance = i - stack[-1] - 1
                min_height = min(arr[stack[-1]], arr[i]) - arr[top_height_idx]
                ans += distance * min_height
            stack.append(i)
        return ans

    def trapping_water_linear(self, arr, n):
        size = n - 1
        prev = arr[0]
        prev_idx = 0
        water = 0
        temp = 0
        for i in range(1, n):
            if arr[i] >= prev:
                # if current is greater than previous then we change prev cause no water stored
                prev = arr[i]
                prev_idx = i
                temp = 0
            else:
                # compute stored water
                water += prev - arr[i]
                # need this variable in case we dont encounter any right bound
                temp += prev - arr[i]

        if prev_idx < size:
            # case we did not encounter last bound, removing last piece from computation
            water -= temp
            prev = arr[size]
            for i in range(size, prev_idx - 1, -1):
                if arr[i] >= prev:
                    prev = arr[i]
                else:
                    water += prev - arr[i]
        return water


print(Solution().trapping_water_linear([8, 8, 2, 4, 5, 5, 1], 7))

