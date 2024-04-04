babbling=["ayayeayaye","mamama" "uuu", "yeye", "yemawoo", "ayay"]
li=["aya","ye","woo","ma"]
answer = 0
for i in babbling:
    for j in li:
        repeats=j+j
        if i in repeats or i=='':
            break
        i=i.replace(j,"")
        
    print(i)
    if i=="":
        answer+=1

# print(answer)


