n=["may", "kein", "kain", "radi"] 
y=[5, 10, 1, 3]
p=[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]


# # 내가 해결한답
# result=[]

# x={ name : y[nu] for nu, name in enumerate(n) }
# for i in p:
#     sum=0
#     for j in i:
#         if j in x:
#             sum+=x[j]
#     result.append(sum)

# print(result)

# 한줄장인의 정답
def answer(n,y,p):
    return [sum( y[n.index(j)] for j in i if j in n) for i in p]

print(answer(n,y,p))
