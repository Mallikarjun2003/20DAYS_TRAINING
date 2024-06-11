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
        print("even=" ,even)
        print("odd=",odd)
        print("diff=" , abs(even - odd))
    
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self, node):
        if not node:
            return True
        return self.height(node.left) == self.height(node.right)
        
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
    
    def level_order(self):
        if self.root:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                print(node.data,end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


bst = BST()
nums = [4, 2, 9, 5,3,6,8]
for i in nums:
    bst.insert(i)
# bst.in_order()
# # bst.pre_order()
# # bst.post_order()
# bst.even_odd_diff()
# bst.sum_of_nodes()
# bst.level_order()
root_height = bst.height(bst.root)
print(root_height)
is_bal =bst.is_balanced(bst.root)
print(is_bal)