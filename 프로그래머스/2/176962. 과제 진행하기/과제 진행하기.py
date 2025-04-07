def solution(plans):
    answer = []
    stack = []
    n=len(plans)
    for i in range(n):
        h,m=map(int,plans[i][1].split(':'))
        start=h*60+m
        plans[i][1]=start
        plans[i][2]=int(plans[i][2])+start
    
    plans.sort(key=lambda x:x[1])
    
    for i in range(1,n):
        beforeName, _, beforeEndTime = plans[i-1]
        currentName, currentStartTime, currentEndTime = plans[i]
        
        if beforeEndTime > currentStartTime:
            remind_time = beforeEndTime-currentStartTime
            stack.append([beforeName,remind_time])
        else:
            answer.append(beforeName)
            if currentStartTime-beforeEndTime>0:
                while stack:
                    remind_name, remind_time = stack.pop()
                    beforeEndTime+=remind_time
                    if currentStartTime>=beforeEndTime:
                        answer.append(remind_name)
                    else:
                        remind_time=beforeEndTime-currentStartTime
                        stack.append([remind_name,remind_time])
                        break
    answer.append(plans[-1][0])
    while stack:
        name,time = stack.pop()
        answer.append(name)
                
    return answer