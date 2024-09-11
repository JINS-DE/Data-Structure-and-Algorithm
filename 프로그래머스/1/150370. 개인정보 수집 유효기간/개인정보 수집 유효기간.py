def solution(today, terms, privacies):
    y,m,d = map(int,today.split('.'))
    today = y*12*28+m*28+d # 오늘 날짜 day로 표현

    terms = {i[:1] : int(i[2:])*28 for i in terms} # terms day로 dic형태로 변환

    answer=[]
    for index,p in enumerate(privacies):
        y,m,d=p.split('.')
        d,c = d.split()

        p=int(y)*12*28+int(m)*28+int(d)

        if today >= p+terms[c] :
            answer.append(index+1)
    
    return answer