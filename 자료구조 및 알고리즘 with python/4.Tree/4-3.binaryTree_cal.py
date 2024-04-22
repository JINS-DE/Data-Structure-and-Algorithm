'''
이진트리의 연산
- 이진트리는 루트와 두 개의 서브 트리로 이루어져있다.
- 이진트리의 표준순회
    - 순회(traversal)한다는 것은 트리의 모든 노드를 한 번씩 방문하는 것을 의미한다.
    - 트리에서는 자료가 일렬로 나열되어 있지 않기에 여러 가지 '순서'로 노드를 방문한다.
    - 기본적으로 전위, 중위, 후위로 나뉜다. => 표준순회
    - 표현법 V(루트) , L(left) , R(right)
        - 전위순회(preorder traversal) : VLR
        - 중위순회(inorder traversal) : LVR
        - 후위순회(postorder traversal) : LRV
- 트리에서는 전체 트리나 서브 트리나 기본 구조가 완전히 같아 순환(재귀) 기법이 흔히 사용된다.
'''

# 1. 전위순회(preorder)
# 루트(V)를 먼저 방문하고 왼쪽 서브 트리 방문(L), 마지막으로 오른쪽 서브 트리를 방문(R)
def preorder(n): #전위 순회 함수
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left) #왼쪽 서브 트리 처리
        preorder(n.right) #오른쪽 서브 트리 처리

# 2. 중위순회(inorder)
# 왼쪽 서브 트리(L)부터 시작 루트(V)를 거쳐 오른쪽 서브 트리(R) 순서
def inorder(n):
    if n is not None:
        inorder(n.left) #왼쪽 서브 트리 처리
        print(n.data, end=' ') # 노드에서 처리할 연산들의 위치
        inorder(n.right) #오른쪽 서브 트리 처리

# 3. 후위순회(postorder)
# 왼쪽 서브 트리 -> 오른쪽 서브 트리 -> 루트
def postorder(n):
    if n is not None:
        postorder(n.left) 
        postorder(n.right) 
        print(n.data, end=' ') # 노드에서 처리할 연산들의 위치
'''
어떤 순회를 써야하는가?
- 순서 상관없이 모든 노드를 방문하기만 한다면 어떤 순회를 써도 상관없다.
- 자식을 먼저 처리해야 하는 컴퓨터 어떤 폴더들의 용량을 계산시에 후위순회를 사용해야 한다.
- 부모가 먼저 처리되어야 자식을 처리할 수 있다면 전위순회를 사용해야 한다.
    예를 들어, 자신의 레벨을 계산하는 경우 전위순회를 사용해야 한다. 루트 레벨이 1이고 나머지 노드는 부모의 레벨보다 1이 크다.


# 레벨 순회(Level order)
- 레벨 순으로 노드를 방문한다. 
- 위에서 아래로, 왼쪽부터 오른쪽 방향으로 방문한다.
- 큐(Queue)를 이용하면 간단하게 해결할 수 있다. 
    so, 레벨 순회는 순환을 사용하지 않는다. 대신 queue를 사용
'''
# 이진 트리의 레벨 순회
from ArrayQueue import ArrayQueue
class BTNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem
        self.left = left # 왼쪽 자식을 위한 링크
        self.right = right # 오른쪽 자식을 위한 링크

def levelorder(root):
    queue = ArrayQueue() 
    queue.enqueue(root)
    while not queue.isEmpty(): # 큐가 공백이 아닌 동안
        n=queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
'''
이진 트리의 연산들
1. 전체 노드의 수 구하기
이진 트리의 노드 개수는 왼쪽 서브 트리의 노드 수와 오른쪽 서브 트리의 노드 수의 합에 1(루트노드)을 더하면 된다.
Total = Left(왼쪽 서브 트리의 전체 노드 수) + Right(오른쪽 서브 트리의 전체 노드 수) + 1

2. 트리의 높이 구하기
이진 트리의 높이는 왼쪽 서브 트리의 높이와 오른쪽 서브 트리의 높이 중 큰 값에 1을 더한 값이다.
height = max(Left,Right)+1
'''
# 이진 트리 전체 노드의 수 구하기
def count_node(n):
    if n is None:
        return 0
    else: return count_node(n.left) + count_node(n.right) + 1

# 이진 트리의 높이 구하기
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left) # 왼쪽 높이
    hRight = calc_height(n.right) # 오른쪽 높이
    if (hLeft>hRight):
        return hLeft + 1
    else : return hRight + 1

# 이진 트리 연산 테스트 프로그램
d = BTNode('D',None,None)
e = BTNode('E',None,None)
b = BTNode('B',d,e)
f = BTNode('F',None,None)
c = BTNode('C',f,None)
root = BTNode('A',b,c)

print('\n In-Order : ', end=''); inorder(root)
print('\n Pre-Order : ', end=''); preorder(root)
print('\n Post-Order : ', end=''); postorder(root)
print('\n Level-Order : ', end=''); levelorder(root)
print()

print(" 노드의 개수 : %d개" % count_node(root))
print(" 트리의 높이 : %d" % calc_height(root))

