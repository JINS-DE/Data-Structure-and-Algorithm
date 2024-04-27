'''
수식 트리(Expression Tree)란 산술식을 트리 형태로 표현한 이진 트리이다.
- 하나의 연산자가 두 개의 피연산자를 갖는다고 가정
- 피연산자는 단말노드에 저장되고 연산자는 루트나 가지노드에 배치한다.

# 수식 트리의 계산
- 어떤 연산자를 계산하려면 자식 노드의 계산이 반드시 끝나 있어야한다.
- 수식 트리의 계산에는 후위순회가 적용

'''
from import_file import BTNode, preorder,inorder,postorder
# 수식 트리 계산 함수
def evaluate(node) :
    if node is None : #공백 트리이면 0 반환
       return 0
    elif node.isLeaf() : # 그 노드 값(데이터) 반환
       return node.data
    else :
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == '+' : return op1 + op2
        elif node.data == '-' : return op1 - op2
        elif node.data == '*' : return op1 * op2
        elif node.data == '/' : return op1 / op2

'''
수식의 표현 방법
- 전위(prefix) : + A B 
- 중위(infix) : A+B
- 후위(postfix) : A B +
=> 컴퓨터는 중위 표기법을 좋아하지 않는다. 처리가 번거로움. 
후위 표기를 사용한다.
- 괄호를 사용하지 않아도 계산 순서를 알 수 있다.
- 연산자의 우선순위를 생각할 필요가 없다. 식 자체에 우선순위가 이미 포함
- 수식을 읽으면서 바로 계산 가능
'''
def buildETree(expr) : #후위 표기 수식을 expr로 전달
    if len(expr) == 0 :
        return None
    token = expr.pop() #후위순회는 수식을 뒤에서 앞으로 처리, 따라서 pop()으로 맨 뒤 요소 꺼냄
    if token in "+-*/" :
        node = BTNode(token)
        node.right = buildETree(expr)
        node.left = buildETree(expr)
        return node
    else:
        return BTNode(float(token))
    
str = input("입력(후위표기): ")		# 후위표기식 입력
expr = str.split()			        # 토큰 리스트로 변환
print("토큰분리(expr): ", expr)
root = buildETree(expr)			    # 후위표기 --> 수식트리
print('\n전위 순회: ', end=''); preorder(root)
print('\n중위 순회: ', end=''); inorder(root)
print('\n후위 순회: ', end=''); postorder(root)
print('\n계산 결과 : ', evaluate(root))	# 수식트리 계산

