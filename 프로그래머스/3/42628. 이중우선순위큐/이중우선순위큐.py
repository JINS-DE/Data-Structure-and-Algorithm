from collections import deque
def solution(operations):
    answer = []
    q=[]
    for oper in operations:
        command,num = oper.split()
        if command=='I':
            q.append(int(num))
        else:
            
            if len(q)==0:
                continue
            q.sort()
            tmp=deque(q)
            if num=="-1":
                tmp.popleft()
            else:
                tmp.pop()
            q=list(tmp)
    if q:
        q.sort()
        return [q[-1],q[0]]
    else:
        return [0,0]