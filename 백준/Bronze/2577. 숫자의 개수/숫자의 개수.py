A=int(input())
B=int(input())
C=int(input())

multi= A*B*C
li=[0 for i in range(10)]

for i in str(multi):
    li[int(i)]+=1
for i in li: print(i)