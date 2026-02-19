#1 frequency map (counting)

freq = {}
for x in [1, 2, 3, 4]:
    freq[x] = freq.get(x, 0) + 1

#2 Two pointers (sorted / apposite ends)

def two_pointer_example(arr, target):
    l, r = 0, len(arr) - 1 
    while l < r:
        s = arr[l] + arr[r]
        if s < target:
            l += 1
        elif s > target:
            r -= 1
        else:
            return (l, r)
        
#3 Sliding window (grow / shrink)

def sliding_window_example(arr, target):
    l = 0 
    for r in range(len(arr)):
        while condition_is_bad():
            l += 1

#4 Stack (matching/monotonic)

stack = []
for x in arr:
    while stack and stack[-1] > x:
        stack.pop()
    stack.append(x)

#5 Prefix sum (fast subarray sums)

prefix = 0
seen = {0: 1}
for x in arr:
    prefix += x
    # use prefix 

#6 BFS (queue)

from collections import deque
q = deque([start])
seen = {start}
while q:
    node = q.popleft()
    for nei in graph[node]:
        if nei not in seen:
            seen.add(nei)
            q.append(nei)

#7 DFS (recursion)

def dfs(node):
    for nei in graph[node]:
        if nei not in seen:
            seen.add(nei)
            dfs(nei)

#8 Binary Search

l, r = 0, len(arr) - 1
while l <= r:
    m = (l + r) // 2
    if arr[m] == target:
        return m
    elif arr[m] < target:
        l = m + 1
    else: 
        r = m - 1
return -1