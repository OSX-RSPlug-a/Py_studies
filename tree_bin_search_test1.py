
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)



def depthSearch(tree):
    if tree is None:
        return
    
    print(tree.value)
    
    for child in tree.children:
        depthSearch(child)



root = Node("A")

child_b = Node("B")
child_c = Node("C")
child_d = Node("D")


root.add_child(child_b)
root.add_child(child_c)
child_b.add_child(child_d)


print("Tree order:")
depthSearch(root)