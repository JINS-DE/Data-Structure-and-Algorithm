s="abracadabra"

compare=""
c_cnt=0
oth_cnt=0
word=0
last_index = len(s)-1
for index,i in enumerate(s):
    if compare=="":
        compare+=i

    if compare==i:
        c_cnt+=1
    else:
        oth_cnt+=1
    
    if c_cnt == oth_cnt:
        word+=1
        c_cnt=0
        oth_cnt=0
        compare=""
    elif index==last_index and c_cnt!=oth_cnt:
        word+=1


print(word)



