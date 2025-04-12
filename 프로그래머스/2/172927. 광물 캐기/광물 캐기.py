def solution(picks, minerals):
    answer = 0
    li=[]
    max_mine = sum(picks) * 5
    minerals = minerals[:max_mine]
    for i in range(0,len(minerals),5):
        tmp=0
        for j in range(i,i+5):
            if j>=len(minerals):
                break
            if minerals[j]=="diamond":
                tmp+=25
            elif minerals[j]=="iron":
                tmp+=5
            else:
                tmp+=1
        li.append((tmp,i))
    li.sort()
    
    for i in range(3):
        for _ in range(picks[i]):
            if li:
                _,idx=li.pop()
                for k in range(idx,idx+5):
                    if k >= len(minerals):
                        break
                    m = minerals[k]
                    if i == 0:
                        answer += 1  
                    elif i == 1:
                        answer += 5 if m == "diamond" else 1
                    elif i == 2:
                        answer += 25 if m == "diamond" else 5 if m == "iron" else 1
                        
            else:
                break

        
        
    return answer