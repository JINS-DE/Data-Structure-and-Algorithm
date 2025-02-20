def solution(numbers):
    result = []
    def count_nodes(x):
        h=1
        total=0
        while True:
            if x<=2**h-1:
                return total
            h+=1
            total=2**h-1
    def solve(nodes):
        length = len(nodes)
        if length==1 or '1' not in nodes or '0' not in nodes:
            return True
        mid = length//2
        
        if nodes[mid]=='0':
            return False
        return solve(nodes[:mid]) and solve(nodes[mid+1:])
    
    for i in numbers:
        tree = bin(i)[2:]
        total_nodes = count_nodes(len(tree))
        tree = '0'*(total_nodes-len(tree)) + tree
        result.append(1 if solve(tree) else 0)
    return result