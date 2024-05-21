today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# # 실패 코드(90점 코드 였음)
# # terms dic로 표현
# terms_dict={}
# for i in terms:
#     term = i.split()
#     terms_dict[term[0]]=int(term[-1])

# t_y,t_m,t_d=map(int,today.split('.')) # 투데이 년,월,일 split

# answer = []
# for index,i in enumerate(privacies):
#     p_split = i.split()
#     term_type=p_split[-1]

#     Y,M,D=map(int,p_split[0].split('.'))
    
#     M=M+terms_dict[term_type]

#     Y+=M//12
#     M=M%12
#     if t_y > Y :
#         answer.append(index+1)
#     elif t_y == Y and t_m > M:
#         answer.append(index+1)
#     elif t_y == Y and t_m == M and t_d >= D :
#         answer.append(index+1)
    
# day 기준으로 변환
y,m,d = map(int,today.split('.'))
today = y*12*28+m*28+d # 오늘 날짜 day로 표현

terms = {i[:1] : int(i[2:])*28 for i in terms} # terms day로 dic형태로 변환

answer=[]
for index,p in enumerate(privacies):
    y,m,d=p.split('.')
    d,c = d.split()
    
    p=int(y)*12*28+int(m)*28+int(d)+terms[c]
    
    if today >= p :
        answer.append(index+1)

print(answer)