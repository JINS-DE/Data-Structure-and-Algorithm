def solution(s):
    size = len(s)

    answer=size
    for i in range(1,size//2+1):
        before = s[:i]
        cnt = 1
        st=''
        for j in range(i,size+1,i):
            now=s[j:j+i]
            if before==now:
                cnt+=1
            else:
                if cnt > 1:
                    st+=str(cnt)+before
                else:
                    st+=before
                before=now
                cnt=1
        if cnt>1:
            st+=str(cnt)+before
        else:
            st+=before
        answer=min(answer,len(st))
                 
    return answer