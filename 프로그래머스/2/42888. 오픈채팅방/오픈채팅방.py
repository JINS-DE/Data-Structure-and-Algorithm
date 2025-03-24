from collections import defaultdict
def solution(records):
    name_dic = defaultdict(str)
    
    output=[]
    
    for record in records:
        re = record.split()
        if len(re)==2:
            output.append(re)
            continue
        command, user_id, nick = re
        name_dic[user_id] = nick
        if command == "Enter":
            output.append([command,user_id])
    result = []
    for o in output:
        if o[0]=="Enter":
            result.append(f"{name_dic[o[1]]}님이 들어왔습니다.")
        else:
            result.append(f"{name_dic[o[1]]}님이 나갔습니다.")
    
            
            
    return result