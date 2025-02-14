from itertools import permutations
def solution(numbers):
    answer=set()
    for i in range(1,len(numbers)+1):
        answer|=set(map(int,map("".join, permutations(numbers,i))))
    answer-=set(range(0,2))
    
    for i in range(2,int(max(answer)**0.5)+1):
        answer-=set(range(i *2 , max(answer) + 1, i))
        
        
        
    return len(answer)