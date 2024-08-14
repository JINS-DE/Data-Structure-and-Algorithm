n=5
n_li=[4,1,5,2,3]
m=5
m_li=[1,3,7,9,5]
n_li.sort()
def binary_search(num):
    pl=0
    pr=len(n_li)-1
    while True:
        pc=(pl+pr)//2
        if n_li[pc]==num:
            return 1
        elif n_li[pc]<num:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl>pr:
            break
    return 0 

for i in m_li:
    print(binary_search(i))

