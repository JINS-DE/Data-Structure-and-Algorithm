"""
전체날짜를 일수로 통합
파기 : TODAY > 계약일 + 유효기간 -1 
"""

def solution(today, terms, privacies):
    answer = []
    terms_dic = {}
    
    y,m,d = today.split('.')
    today = int(y[2:])*12*28 + int(m)*28 + int(d)
    
    for term in terms:
        rule, deadline = term.split()
        terms_dic[rule] = int(deadline)*28
    
    answer=[]
    for i, privacy in enumerate(privacies):
        date, rule = privacy.split()
        y, m ,d = date.split('.')
        deadline = int(y[2:])*12*28 + int(m)*28 + int(d) + terms_dic[rule] -1
        if today > deadline:
            answer.append(i+1)
            
    return answer