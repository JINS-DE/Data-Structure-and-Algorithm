import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
answer=0
def dfs(depth, current_sum):
    global answer

    if depth == n :
        if current_sum == m:
            answer+=1
        return
    dfs(depth+1,current_sum)
    dfs(depth+1, current_sum+arr[depth])

dfs(0,0)


if m == 0:
    answer -= 1

print(answer)