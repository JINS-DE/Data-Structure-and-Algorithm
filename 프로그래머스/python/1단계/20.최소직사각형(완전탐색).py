def solution(sizes):
    w1=0
    h1=0
    w2=0
    h2=0

    for i in sizes:
        w2=i[0]
        h2=i[1]
        w1=max(max(w1,h1),max(w2,h2))
        h1=max(min(w1,h1),min(w2,h2))
    return w1*h1
