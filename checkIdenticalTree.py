class Node(object):
    def __init__(self, data):
        self.data = data
	self.left = None
	self.right = None

def isIdentical(root1, root2):
    if not root1 and not root2:
        return True
    # Following condition should be true for identical
    a = (root1.data == root2.data)
    b = isIdentical(root1.left, root2.left)
    c = isIdentical(root1.right, root2.right)
    if a and b and c:
        return True
    return False

# Convert to iteration
def iterative(root1, root2):
    if not root1 and not root2:
        return True
    stack = []
    stack.append((root1, root2))
    while len(stack):
        root1, root2 = stack[-1] # Top of stack
	while root1.left and root2.left:
	    stack.append((root1.left, root2.left))
	    root1 = root1.left
	    root2 = root2.left
	if root1.left or root2.left: # if any of defined
	    return False
	root1, root2 = stack.pop()
	if root1.data == root2.data:
	    root1 = root1.right
	    root2 = root2.right
	    if root1 and root2:
	        stack.append((root1, root2))
		continue
	    elif not root1 and not root2:
	        continue
	    else:
	        return False
	else:
	    return False
    return True


if __name__ == '__main__':
    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.right = Node(3)
    tree1.left.left = Node(4)
    tree1.left.right = Node(5)
    tree2 = Node(1)
    tree2.left = Node(5)
    tree2.right = Node(3)
    tree2.left.left = Node(4)
    tree2.left.right = Node(5)
    #print isIdentical(tree1, tree2)
    print iterative(tree1, tree2)
