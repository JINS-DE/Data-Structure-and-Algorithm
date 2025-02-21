def solution(commands):
    table=[["EMPTY"]*51 for _ in range(51)]
    parent = [[(r, c) for c in range(51)] for r in range(51)]
    result = []
    
    def find(r, c) :
        if (r, c) == parent[r][c] :
            return parent[r][c]
        pr, pc = parent[r][c]
        parent[r][c] = find(pr, pc)
        return parent[r][c]
    
    def union(r1, c1, r2, c2):
        pr1, pc1 = find(r1, c1)
        pr2, pc2 = find(r2, c2)
        parent[pr2][pc2] = (pr1, pc1)

    def UPDATE_ONE(r, c, val):
        pr, pc = find(r, c)
        table[pr][pc] = val

    def UPDATE_ALL(val1, val2):
        for r in range(51):
            for c in range(51):
                pr, pc = find(r, c)
                if table[pr][pc] == val1:
                    table[pr][pc] = val2

    def MERGE(r1, c1, r2, c2):
        r1, c1 = find(r1, c1)
        r2, c2 = find(r2, c2)

        if (r1, c1) == (r2, c2):
            return
        
        # 값이 있는 쪽을 유지
        if table[r1][c1] == "EMPTY":
            table[r1][c1] = table[r2][c2]

        union(r1, c1, r2, c2)

    def UNMERGE(r, c):
        pr, pc = find(r, c)
        val = table[pr][pc]
        
        merge_list = []
        for i in range(51):
            for j in range(51):
                if find(i, j) == (pr, pc):
                    merge_list.append((i, j))
        
        for x, y in merge_list:
            parent[x][y] = (x, y)
            table[x][y] = "EMPTY"
        
        table[r][c] = val  # 원래 값 유지
    
    def PRINT(r, c):
        pr, pc = find(r, c)
        result.append(table[pr][pc])

    for command in commands:
        command = command.split()
        
        if command[0] == 'UPDATE':
            if len(command) == 4:
                UPDATE_ONE(int(command[1]), int(command[2]), command[3])
            else:
                UPDATE_ALL(command[1], command[2])
        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, command[1:])
            MERGE(r1, c1, r2, c2)
        elif command[0] == 'UNMERGE':
            r, c = map(int, command[1:])
            UNMERGE(r, c)
        elif command[0] == 'PRINT':
            r, c = map(int, command[1:])
            PRINT(r, c)

    return result
