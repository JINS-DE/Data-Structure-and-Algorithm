def isGood(word):
    stack=[]
    for w in word:
        if w=='(':
            stack.append('(')
        elif stack:
            stack.pop()
        else:
            return False
    if stack:
        return False
    else:
        return True


def recur(w):
        if w=="":
            return ""
        
        l_cnt=r_cnt=0
        for i,val in enumerate(w):
            if val=='(':
                l_cnt+=1
            else:
                r_cnt+=1
            
            if l_cnt == r_cnt:
                u = w[:i+1]
                v = w[i+1:]
                break
                
        if isGood(u):
            return u+recur(v)
        else:
            
            tmp= '('+recur(v)+')'
            st=''
            for r_u in u[1:-1]:
                if r_u=='(':
                    st+=')'
                else:
                    st+='('
            st=tmp+st
            return st 
    
def solution(p):
    
    return recur(p)