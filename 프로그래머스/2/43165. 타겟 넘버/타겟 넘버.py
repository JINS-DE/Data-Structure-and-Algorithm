
def solution(numbers, target):
    answer=0
    N = len(numbers)
    def dfs(depth,SUM):
        nonlocal answer
        if depth == N:
            if SUM==target:
                answer+=1
            return
        
        dfs(depth+1,SUM+numbers[depth])
        dfs(depth+1,SUM-numbers[depth])
        
            
    dfs(0,0)
    return answer