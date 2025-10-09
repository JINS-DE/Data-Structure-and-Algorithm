"""
1. number를 포화 이진트리로 만든다.
2. 포화 이진트리의 이진트리가 성립되는지 확인한다. 
"""
    
def solution(numbers):
    def to_full_binary(x):
        h=1
        total=0
        while True:
            if x<=2**h-1:
                return total
            h+=1
            total=2**h-1
        

    def is_binary_search(binary):
        length = len(binary)
        mid = length//2
        if not binary or length==1 or '1' not in binary or '0' not in binary:
            return True
        
        if binary[mid]=='0':
            return False
        
        return is_binary_search(binary[:mid]) and is_binary_search(binary[mid+1:])
    
    answer = []
    for num in numbers:
        if num==1:
            answer.append(1)
            continue
        binary = bin(num)[2:]
        length = len(binary)
        total_size = to_full_binary(length)
        binary = '0'*(total_size-length) + binary
        answer.append(1 if is_binary_search(binary) else 0 )
    
    return answer