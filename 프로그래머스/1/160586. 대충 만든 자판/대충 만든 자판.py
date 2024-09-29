def solution(keymap, targets):
    answer = []
    def test(target):
        li=[]
        for i in keymap:
            li.append(i.find(target))

        if min(li) >= 0 :
            return min(li)+1
        else:
            if max(li)==-1:
                return -1
            else:
                return min(filter(lambda x: x>-1 , li))+1




    for i in targets:
        cnt=0
        for j in i:
            if test(j)==-1:
                cnt=-1
                break
            cnt+=test(j)
        answer.append(cnt)
    return answer