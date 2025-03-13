from itertools import permutations
def solution(expression):
    answer = []
    operator={'-','+','*'}
    st=''
    arr=[]
    for s in expression:
        st+=s
        if s in operator:
            arr.append(int(st[:-1]))
            arr.append(st[-1])
            st=''
    arr.append(int(st))
    

    for permu in permutations(operator,3):      
        li=arr[:]
        for op in permu:
            new_li=[]
            cnt=0
            while cnt<len(li):
                if li[cnt]==op:
                    a=new_li.pop()
                    b=li[cnt+1]
                    if op=='+':
                        new_li.append(a+b)
                    elif op =='-':
                        new_li.append(a-b)
                    elif op == '*':
                        new_li.append(a*b)
                    cnt+=1
                else:
                    new_li.append(li[cnt])
                cnt+=1
                print(li)
            li = new_li
            print(li)
        answer.append(abs(int(li[0])))
        print(answer)
    return max(answer)