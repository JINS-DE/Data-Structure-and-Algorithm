s="banana"
result=[]
test = ""
for index,i in enumerate(s):
    if test.find(i) == -1:
        result.append(test.find(i))
    else:
        result.append(index-test.rfind(i))
    test+=i
print(result)

