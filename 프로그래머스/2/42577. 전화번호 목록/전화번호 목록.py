def solution(phone_book):
    phone_book = set(phone_book)
    for key in phone_book:
        tmp = ""
        for num in key:
            tmp+=num
            if tmp!=key and tmp in phone_book:
                return False
    
    return True