import sys
sys.setrecursionlimit(3000)
def solution(n, m, x, y, r, c, k):
    
    # sorted_direct = ['d', 'l', 'r', 'u']
    direct = {'d':(1,0),'l':(0,-1),'r':(0,1),'u':(-1,0)}
    # 격자크기 : n,m
    # 출발 : x,y
    # 도착 : r,c
    # 이동 거리 : k
    answer=[]
    min_dist = abs(x - r) + abs(y - c)
    
    # 도달할 수 없는 경우 (k와 최단 거리의 홀짝성이 다르면 불가능)
    if min_dist > k or (k - min_dist) % 2 == 1:
        return "impossible"
    for st,d in direct.items():
        dr,dc = d
        # nr = pr+dr
        # nc = pc+dc
    def dfs(depth,pr,pc,path):
        if depth==k:            
            if pr == r and pc == c:
                return path
            return ""
        for st,d in direct.items():
            dr,dc = d
            nr = pr+dr
            nc = pc+dc
            min_dist = abs(nr-r)+abs(nc-c)
            if 1<=nr<=n and 1<=nc<=m and min_dist <= k-depth-1:
                ans = dfs(depth+1,nr,nc,path+st)
                if ans!="":
                    return ans
        return ""
    
    answer = dfs(0,x,y,"")

    if answer== "":
        return "impossible"
    else:
        return answer
