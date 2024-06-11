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
        print("IN ORDER ")
        def traverse(root):
            if root :
                traverse(root.left)
                print(root.data,end=" ")
                traverse(root.right)
        
        traverse(self.root)
        print()
    def pre_order(self):
        print("PRE ORDER ")
        def traverse(root):
            if root: 
                print(root.data,end=" ")
                traverse(root.left)
                traverse(root.right)
        
        traverse(self.root)
        print()

    def post_order(self):
        print("POST ORDER ")
        def traverse(root):
            if root: 
                traverse(root.left)
                traverse(root.right)
                print(root.data,end=" ")
        traverse(self.root)
        print()

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
    def sum_of_nodes(self):
        sum = 0
        def traverse(root):
            nonlocal sum
            if root:
                sum += root.data
                traverse(root.left)
                traverse(root.right)
            return sum
        sum = traverse(self.root)
        print(sum)

bst = BST()
nums = [4, 2, 9, 5]
for i in nums:
    bst.insert(i)
bst.in_order()
bst.pre_order()
bst.post_order()
# bst.even_odd_diff()
bst.sum_of_nodes()