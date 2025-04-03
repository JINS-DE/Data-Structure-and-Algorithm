def change(st):
    lst=[]
    tmp=''
    for s in st:
        if not s.isalpha():
            tmp=''
            continue
        tmp+=s.lower()
        if len(tmp)==3:
            tmp=tmp[1:]
            lst.append(tmp)     
        elif len(tmp)==2:
            lst.append(tmp)
    return lst



from collections import defaultdict
def solution(str1, str2):
    answer = 0
    s1=change(str1)
    s2=change(str2)
    if len(s1)==0 and len(s2)==0: return 65536
    print("s1:",s1,"s2:",s2)
    ele_dict= defaultdict(int)
    intersec=[]
    for i in s1:
        ele_dict[i]+=1
    union=s1
    
    
    for j in s2:
        if ele_dict[j]:
            ele_dict[j]-=1
            intersec.append(j)
        else:
            union.append(j)
    
    
    
    return int(len(intersec)/len(union)*65536)