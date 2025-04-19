from collections import deque
def solution(begin, target, words):
    def compare_word(a,b):
        n=len(a)
        cnt=0
        for i in range(n):
            if a[i]!=b[i]:
                cnt+=1
            if cnt>1:
                return False
        return True
    
    if target not in words:
        return 0

    visited=[0]*len(words)
    q=deque([(0,begin)])
    while q:
        cnt,w = q.popleft()
        if w==target:
            return cnt
        for i,word in enumerate(words):
            if visited[i] or not compare_word(w,word):
                continue
            visited[i]=1
            q.append((cnt+1,word))