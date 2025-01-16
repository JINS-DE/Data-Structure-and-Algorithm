import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort()

answer_li = []
curr_start, curr_end = arr[0]  

for i in range(1, n):
    start, end = arr[i]
    if start <= curr_end:  
        curr_end = max(curr_end, end)  
    else:
        answer_li.append((curr_start, curr_end)) 
        curr_start, curr_end = start, end 

answer_li.append((curr_start, curr_end))

answer = sum(e - s for s, e in answer_li)
print(answer)
