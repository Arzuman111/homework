class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None    


    def add(self,value):
        """

        """
        if self.root is None:
            self.root =Node(value)
        else:
            temp = self.root
            while True:
                if temp.value < value  and temp.right is  not None:
                    temp = temp.right
                elif temp.value < value  and temp.right is None:
                    temp.right = Node(value)
                    break
                if temp.value > value  and temp.left is  not None:
                    temp = temp.left
                elif temp.value > value  and temp.left is None:
                    temp.left = Node(value)    
                    break


    def find(self,value):
        """

        """
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return temp
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return None        
    

    def delete(self, value): 
        """
        
        """
        straight = '' 
        previous = self.root 
        temp = self.root  
        while temp is not None: 
            if value == temp.value: 
                if temp.right is not None and temp.left is None: 
                    if straight == 'left': 
                        previous.left = temp.right 
                    else: 
                        previous.right = temp.right 
                elif temp.left is not None and temp.right is None: 
                    if straight == 'left': 
                        previous.left = temp.left 
                    else: 
                        previous.right = temp.left 
                else: 
                    temp1 = temp.right 
                    if temp1.left is None: 
                        temp.value = temp1.value 
                    else: 
                        while temp1.left is not None: 
                            temp1 = temp1.left 
                        temp.value = temp1.value 
            elif value < temp.value: 
                straight = 'left' 
                previous = temp 
                temp = temp.left  
            else: 
                straight = 'right' 
                previous= temp  
                temp = temp.right
              


    # root -> left -> right
    def preorder_traverse(self, node,value):
        if node is not None:
            if node.value == value:
                return True
            if self.preorder_traverse(node.left, value):
                return True
            if self.preorder_traverse(node.right, value):
                return True
        return False    
            # print(node.value)
            # self.preorder_traverse(node.left)
            # self.preorder_traverse(node.right)


    # left-> root-> right
    # prints tree in sorted order
    def inorder_traverse(self,node):
        if node is not None:
            self.inorder_traverse(node.left)
            print(node.value)
            self.inorder_traverse(node.right)


    # left-> right-> root        
    def postorder_traverse(self,node):
        if node is not None:
            self.postorder_traverse(node.left)
            self.postorder_traverse(node.right)
            print(node.value)


tree = BinaryTree()
tree.add(8)
tree.add(3)
tree.add(1)
tree.add(6)
tree.add(4)
tree.add(7)
tree.add(10)
tree.add(14)
tree.add(13)
tree.add(12)


# tree.preorder_traverse(tree.root)

# tree.inorder_traverse(tree.root)

# tree.postorder_traverse(tree.root)

# tree.delete(6)
# tree.inorder_traverse(tree.root)

if tree.preorder_traverse(tree.root,10):
    print("there is 10")
else:
    print("there is not 10")    



