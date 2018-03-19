# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

# Node is defined as

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

nodes = []

def inOrderTraversal(node):
    if node is None:
        return
	inOrderTraversal(node.left)
	nodes.append(node.data)
	inOrderTraversal(node.right)

def right(root, pdata):
    if (root is None):
        return True
    if (root.data <= pdata):
        return False
    return right(root.right, root.data) and right(root.right, pdata) \
           and right(root.left, pdata) and left(root.left, root.data)

def left(root, pdata):
    if (root is None):
        return True
    if (root.data >= pdata):
        return False
    return left(root.left, root.data) and left(root.left, pdata) \
           and left(root.right, pdata) and right(root.right, root.data)


def checkBST(root):
    return left(root.left, root.data) and right(root.right, root.data)

    # inOrderTraversal(root)
    # for i in range(1, len(nodes)):
    #     if nodes[i] <= nodes[i-1]:
    #         return False
    # return True

