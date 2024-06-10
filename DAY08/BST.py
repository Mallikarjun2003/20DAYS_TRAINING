class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        def insert_node(node, data):
            if node is None:
                return Node(data)
            elif node.data > data:
                node.left = insert_node(node.left, data)
            else:
                node.right = insert_node(node.right, data)
            return node
        
        self.root = insert_node(self.root, data)
    
    def in_order(self):
        def traverse(root):
            if root is None:
                return 
            traverse(root.left)
            print(root.data)
            traverse(root.right)
        
        traverse(self.root)
    def even_odd_diff(self):
        even = odd = 0
        def even_odd(node):
            nonlocal even
            nonlocal odd

            if not node:
                return
            elif node.data %2 :
                odd += node.data
                even_odd(node.left)
                even_odd(node.right)
            else:
                even += node.data
                even_odd(node.left)
                even_odd(node.right)
        even_odd(self.root)
        print(abs(even - odd))

bst = BST()
nums = [4, 2, 9, 5]
for i in nums:
    bst.insert(i)
bst.in_order()
bst.even_odd_diff()