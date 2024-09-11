def solution(survey, choices):
    result = ''
    score_li_f=[3,2,1,0,-1,-2,-3]
    score_li_r=[-3,-2,-1,0,1,2,3]
    dic={"RT":0,"CF":0,"JM":0,"AN":0}

    for i,s in enumerate(survey):
        if s in dic:
            dic[s]+=score_li_f[choices[i]-1]
        else:
            dic[s[::-1]]+=score_li_r[choices[i]-1]

    for k,v in dic.items():

        if v < 0 :
            result+=k[1]
        else:
            result+=k[0]
    return result