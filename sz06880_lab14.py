# Lab 14

# we are using class and self approach for inputting!
class Node:
   def __init__(self, key):
       self.left = None
       self.right = None
       self.val = key

def insert(bst, key):
    if bst == None:
        return Node(key)
    else:
        if (bst.val < key) or (bst.val == key):
            bst.right = insert(bst.right, key)
        if bst.val > key:
            bst.left = insert(bst.left, key)
    return bst

def exist(bst,key):
	if (bst == None) or (bst.val == key):
		return bst
	if bst.val < key:
		return exist(bst.right,key)
	return exist(bst.left,key)

def maximum(bst,starting_node):
    key = starting_node 
    homo = exist(bst,key)
    while(homo.right):
        homo=homo.right
    return homo

def minimum(bst,starting_node):
    key = starting_node
    homo = exist(bst,key)
    while(homo.left):
        homo=homo.left
    return homo

def inorder_traversal(bst):
    if bst:
        inorder_traversal(bst.left)
        print(bst.val,end=" ")
        inorder_traversal(bst.right)
      
def preorder_traversal(bst):
    if bst:
        print(bst.val,end=" ")
        preorder_traversal(bst.left)
        preorder_traversal(bst.right)
      

def postorder_traversal(bst):
   	if bst:
   		postorder_traversal(bst.left)
   		postorder_traversal(bst.right)
   		print(bst.val,end=" ")


r = Node(68)
r = insert(r, 88)
r = insert(r, 61)
r = insert(r, 89)
r = insert(r, 94)
r = insert(r, 50)
r = insert(r, 4)
r = insert(r, 76)
r = insert(r, 66)
r = insert(r, 82)


node = exist(r,50)
if (node):
	print(node.val," exists")
else:
	print(node.val,"not exists")

  
node=exist(r,49)
if(node):
	print(node.val," exists")
else:
	print("Not exists")

print(minimum(r,68).val)
print(minimum(r,88).val)

print(maximum(r,68).val)
print(maximum(r,61).val)

preorder_traversal(r)
print()
inorder_traversal(r)
print()
postorder_traversal(r)