def solution(files):
    answer = []
    for file in files:
        head=''
        num=''
        tail=''
        flag=0
        for f in file:
            if flag == 0 and f.isdigit():
                flag=1
            if flag == 1 and not f.isdigit():
                flag=2
                
            if flag==0:
                head+=f
            elif flag==1:
                num+=f
            else:
                tail+=f
        answer.append((head,num,tail,int(num),head.upper()))
        # print(head,num,tail)
    answer.sort(key = lambda x : (x[4],x[3]))
    result = []
    for a in answer:
        result.append(''.join(a[:3]))
              
    return result