# def search(number) :
#     length = len(number)
#     if length == 1 or '1' not in number or '0' not in number:
#         return True
    
#     mid = length // 2
#     if number[mid] == '0':
#         return False
    
#     return search(number[:mid]) and search(number[mid+1:])

# numbers=[58,113,4423]
# bin_numbers = [ bin(x)[2:] for x in numbers]
# bin_list = [ 2**x - 1 for x in range(50)]
# answer=list()
# for number in bin_numbers :
#     length = len(number)
#     for num in bin_list:
#         if num>= length:
#             number = '0'*(num-length) + number
#             break
#     answer.append(1 if search(number) else 0)


numbers = [32768,3771,7, 42, 5]
answer=[]
def length_(x):
    cnt=0
    s=0
    while True:
        if 2**cnt-1 >= x:
            return cnt
        cnt+=2**s
        s+=1

def solve(num):
    length=len(num)
    if length==1 or '1' not in num or '0' not in num:
        return True
    
    mid = length//2

    if num[mid]=='0':
        return False
    return solve(num[:mid]) and solve(num[mid+1:])
    
for i in numbers:
    max_len=length_(i)
    t=bin(i)[2:]
    if len(t)<max_len:
        t='0'*(max_len-len(t))+t
    answer.append(1 if solve(t) else 0 )    

print(2**15)

