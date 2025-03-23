from itertools import combinations

def is_unique(relation, cols):
    seen = set()
    for row in relation:
        key = tuple( row[c] for c in cols )
        if key in seen:
            return False
        seen.add(key)
    return True
        

def is_minimal(candidates, new_candidate):
    for candidate in candidates:
        is_subset = True
        for col in candidate:
            if col not in new_candidate:
                is_subset = False
                break
        if is_subset:
            return False  
    return True
        

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    candidates = []

    for r in range(1, col_len + 1):
        for cols in combinations(range(col_len), r):
            if is_unique(relation, cols) and is_minimal(candidates, cols):
                candidates.append(cols)  
                
    return len(candidates)
