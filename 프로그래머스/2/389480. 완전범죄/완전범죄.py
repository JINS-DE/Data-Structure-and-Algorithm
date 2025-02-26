def solution(info, n, m):
    dic = {0:0}
    for a,b in info:
        tmp = {}
        for aa, bb in dic.items():
            if aa+a<n:
                if aa+a not in tmp or tmp[aa+a] > bb:
                    tmp[aa+a]=bb
            if bb+b<m:
                if aa not in tmp or tmp[aa] > bb+b:
                    tmp[aa]=bb+b
        if tmp:
            dic=tmp
        else:
            return -1
    return min(dic.keys())