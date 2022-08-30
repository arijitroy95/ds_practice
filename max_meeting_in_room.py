"""
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i])
where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held
in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


Example 1:

Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output:
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)
Example 2:

Input:
N = 3
start[] = {10, 12, 20}
end[] = {20, 25, 30}
Output:
1
Explanation:
Only one meetings can be held
with given start and end timings.
"""
from typing import List


class Meet:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def max_meets(arr: List[Meet], n) -> int:
    arr.sort(key=lambda x: x.end)
    num_meetings = 1
    last_meeting_end_time = arr[0].end
    for i in range(1, n):
        if arr[i].start > last_meeting_end_time:
            num_meetings += 1
            last_meeting_end_time = arr[i].end
    return num_meetings


start = [10, 12, 20]  # [1,3,0,5,8,5]
end = [20, 25, 30]  # [2,4,6,7,9,9]
n = 3
l = []
for i in range(n):
    l.append(Meet(start[i], end[i]))
print(max_meets(l, n))
