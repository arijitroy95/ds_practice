"""
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative numbers without changing the relative order of
positive and negative numbers.
Note: Array should start with positive number.


Example 1:

Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Explanation : Positive elements : 9,4,5,0,2
Negative elements : -2,-1,-5,-3
As we need to maintain the relative order of
postive elements and negative elements we will pick
each element from the positive and negative and will
store them. If any of the positive and negative numbers
are completed. we will continue with the remaining signed
elements.The output is 9,-2,4,-1,5,-5,0,-3,2.


Example 2:

Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
Explanation : Positive elements : 5,2,4,7,1,8,0
Negative elements : -5,-2,-8
As we need to maintain the relative order of
postive elements and negative elements we will pick
each element from the positive and negative and will
store them. If any of the positive and negative numbers
are completed. we will continue with the remaining signed
elements.The output is 5,-5,2,-2,4,-8,7,1,8,0.
"""


def enqueue(queue, val):
    queue.append(val)


def dequeue(queue):
    if queue:
        return queue.pop(0)


def queue_front(queue):
    return queue[0]


def check_last(array):
    if array[-1] >= 0:
        return True
    else:
        return False


def rearrange(arr, n):
    queue = []
    last_val = True
    new_arr = []
    for i in range(n):
        val = arr[i]
        if val >= 0 and not new_arr:
            new_arr.append(val)
            q_top = dequeue(queue)
            if q_top is not None:
                new_arr.append(q_top)
            last_val = check_last(new_arr)
        elif new_arr and ((last_val and val < 0) or (not last_val and val >= 0)):
            new_arr.append(val)
            last_val = check_last(new_arr)
            if queue and ((queue_front(queue) >= 0 and not last_val) or (queue_front(queue) < 0 and last_val)):
                q_top = dequeue(queue)
                new_arr.append(q_top)
            last_val = check_last(new_arr)
        else:
            enqueue(queue, val)
    if queue:
        new_arr.extend(queue)
    return new_arr
