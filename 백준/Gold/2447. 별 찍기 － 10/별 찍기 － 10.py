import sys
input = sys.stdin.readline
N=int(input())

def recur(n):
    if n==1:
        return ['*']
    stars = recur(n//3)
    lst = []
    for star in stars:
        lst.append(star*3)
    
    for star in stars:
        lst.append(star+" "*(n//3)+star)
    
    for star in stars:
        lst.append(star*3)
    
    return lst

print('\n'.join(recur(N)))
