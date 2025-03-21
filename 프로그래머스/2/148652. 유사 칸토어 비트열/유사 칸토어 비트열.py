def is_one(num):
    while num:
        if num%5==2:
            return 0
        num//=5
    return 1
def solution(n, l, r):
    return sum([is_one(i) for i in range(l-1,r)])