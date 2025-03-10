def solution(n, k):
    def is_prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    
    def convert_base(num,k):
        temp=''
        while num>0:
            temp+=str(num%k)
            num//=k
        return temp[::-1]
    
    answer=0
    num_list=list(filter(lambda x:x!='' and x!='1',convert_base(n,k).split('0')))
    
    for i in num_list:
        if is_prime(int(i)):
            answer+=1
            
    return answer