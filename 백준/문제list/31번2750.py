# li=[5,2,3,4,1]
# n=len(li)

# # 버블 정렬
# n=int(input())
# a=[int(input()) for i in range(n)]
# for i in range(n-1):
#     for j in range(n-1-i):
#         if a[j] > a[j+1]:
#             a[j+1],a[j] = a[j],a[j+1]
# for i in a:
#     print(i)

# # 단순 선택 정렬
# n=int(input())
# a=[int(input()) for i in range(n)]
# for i in range(n-1):
#     min_ = i
#     for j in range(i+1,n):
#         if a[j] < a[min_]:
#             min_ = j
#     a[i],a[min_] = a[min_],a[i]

for i in a:
    print(i)

# 단순 삽입 정렬
n=int(input())
a=[int(input()) for i in range(n)]
for i in range(1,n):
    j=i
    tmp=a[i]
    while j>0 and a[j-1]>tmp:
        a[j]=a[j-1]
        j-=1
    a[j]=tmp

for i in a:
    print(i)
