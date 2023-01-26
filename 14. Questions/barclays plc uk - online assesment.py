"""
Allie is working on a system that can allocate resources to the 
applications in a manner efficient enough to allow the maximum number 
of applications to be executed. There are N number of applications 
and each application is identified by a unique integer ID (1 to N). 
Only M types of resources are available with a unique resourceD. 
Each application sends a request message to the system. 
The request message includes the information regarding the request time, 
the execution ending time, and the type of resource required for execution. 
Time is in the MMSS format where MM is minutes and SS is seconds.

If more than one application sends a request at the same time then only 
one application will be approved by the system. The denied requests are 
automatically destroyed by the system. When approving the request, the 
system ensures that the request will be granted to the application in a 
way that will maximize the number of executions. The system can execute 
only one application at a time with a given resource. It will deny all 
other requests for the resource until the previous application has finished. 
Allie wants to know the maximum number of applications that have been 
executed successfully.

Write an algorithm to help Allie calculate the maximum number of applications 
that are executed successfully by the system.

Input
The first line of the input consists of two space-separated integers num and 
constX, representing the number of applications (N) and constX is always 3. 
The next N lines consist of constX space-separated integers representing the 
request time, the execution ending time, and the resourceD of the resource 
required by each application for successful execution.

Output
Print an integer representing the maximum number of applications that are 
executed successfully by the system.


Testcase 1 | Answer: 4
4 3
1000 1020 3
1020 1030 3
1030 1040 3
1010 1045 2

Testcase 2 | Ans: 3
5 3
1200 1230 1
1120 1125 2
1015 1230 1
1100 1230 1
1200 1230 3

Testcase 3 | Ans: 4
6 3
1200 1250 1
1210 1220 1
1225 1230 1
1330 1345 2
1330 1340 2
1340 1345 2
"""


# to bucket all requests by resource type
def bucketRequestsByResource(arr):
    buckets = dict()
    for each_req in arr:
        if buckets.get(each_req[2], False) != False:
            buckets[each_req[2]].append((each_req[0], each_req[1]))
        else:
            buckets[each_req[2]] = [(each_req[0], each_req[1])]
    
    return buckets


# to get max number of executed tasks for a single bucket
def numExecutedAppsByBucket(arr):
    arr.sort(key = lambda x: x[0])
    N = len(arr)
    dont_execute = 0
    latest_end = arr[0][1]

    for i in range(1, N):
        if arr[i][0] < latest_end:
            dont_execute += 1
            latest_end = min(arr[i][1], latest_end)
        else:
            latest_end = arr[i][1]

    return (N - dont_execute)


# get the maximum number of executed tasks
def numExecutedApps(arr):
    buckets = bucketRequestsByResource(arr)
    num_execute = 0
    for each_bucket in buckets.values():
        num_execute += numExecutedAppsByBucket(each_bucket)

    return num_execute
        

# driver code
arr = []
arr_rows, arr_cols = map(int, input().split())
for idx in range(arr_rows):
    arr.append(list(map(int, input().split())))

result = numExecutedApps(arr)
print (result)

