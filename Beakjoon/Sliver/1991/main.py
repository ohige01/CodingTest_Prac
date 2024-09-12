import sys

node_list = []
dict = {}
for i in range(int(input())):
    root, left, right= map(str, sys.stdin.readline().split())
    dict[root] = [left, right]

preOrder_list = []
def preOrder(node):
    preOrder_list.append(node)
    for new_node in dict.get(node):
        if(new_node != '.'):
            preOrder(new_node)

inOrder_list = []
def inOrder(node):
    index = 0
    for new_node in dict.get(node):
        # 왼쪽을 돌고 나서 실행
        if(index == 1):
            inOrder_list.append(node)
        # 왼쪽 오른쪽 파악
        index += 1
        if(new_node != '.'):
            inOrder(new_node)
        
postOrder_list = []
def postOrder(node):
    for new_node in dict.get(node):
        if(new_node != '.'):
            postOrder(new_node)
    postOrder_list.append(node)
    

preOrder('A')
inOrder('A')
postOrder('A')

for node in preOrder_list:
    print(node, end="")
print()

for node in inOrder_list:
    print(node, end="")
print()

for node in postOrder_list:
    print(node, end="")
print()