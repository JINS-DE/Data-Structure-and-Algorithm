x = []  
for i in range(9):
    x.append(int(input()))
print(max(x))
print(x.index(max(x))+1)
