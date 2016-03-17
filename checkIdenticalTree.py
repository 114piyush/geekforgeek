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
    print isIdentical(tree1, tree2)
