"""
Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time.
We earn the profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.


Example 1:

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).
Example 2:

Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).
"""
import heapq


class Job:
    def __init__(self, job_id, deadline, profit):
        self.profit = profit
        self.deadline = deadline
        self.id = job_id

    def __repr__(self):
        return f"{self.id}@{self.deadline}@{self.profit}"


def job_scheduling(jobs, n):
    jobs.sort(key=lambda x: x.deadline)
    num_jobs = 0
    total_profit = 0
    profit_max_heap = []
    for i in range(n - 1, -1, -1):
        if i == 0:
            gap_between_job = jobs[i].deadline
        else:
            gap_between_job = jobs[i].deadline - jobs[i - 1].deadline
        heapq.heappush(profit_max_heap, (-jobs[i].profit, jobs[i].deadline, jobs[i].id))
        while gap_between_job and profit_max_heap:
            profit, deadline, job_id = heapq.heappop(profit_max_heap)
            gap_between_job -= 1
            num_jobs += 1
            total_profit += profit * (-1)
    # result.sort(key=lambda x: x.deadline)
    return num_jobs, total_profit


N = int(input())
info = list(map(int, input().strip().split()))
JOBS = [Job(info[3*i], info[3*i + 1], info[3*i + 2]) for i in range(N)]
print(job_scheduling(JOBS, N))
