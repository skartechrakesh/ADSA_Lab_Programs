class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:

    # Insert
    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    # Search
    def search(self, root, value):
        if root is None:
            print("Not Found")
            return
        if root.value == value:
            print("Found")
            return
        if value < root.value:
            self.search(root.left, value)
        else:
            self.search(root.right, value)

    # Delete
    def delete(self, root, value):
        if root is None:
            return None

        if value < root.value:
            root.left = self.delete(root.left, value)

        elif value > root.value:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = root.right
            while successor.left:
                successor = successor.left

            root.value = successor.value
            root.right = self.delete(root.right, successor.value)

        return root

    # Traversals
    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.value] + self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return []
        return [root.value] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.value]


# -------- Main Program --------
tree = BST()
root = None

# Input
n = int(input("Enter number of elements: "))
values = list(map(int, input("Enter elements (space separated): ").split()))

for i in values[:n]:
    root = tree.insert(root, i)

# Initial Traversals
print("\nTraversals after insertion")
print("Inorder  :", tree.inorder(root))
print("Preorder :", tree.preorder(root))
print("Postorder:", tree.postorder(root))

# Operations
while True:
    print("\n1.Search  2.Delete  3.Exit")
    choice = int(input("Choice: "))

    if choice == 1:
        tree.search(root, int(input("Enter value: ")))

    elif choice == 2:
        root = tree.delete(root, int(input("Enter value: ")))
        print("\nTraversals after deletion")
        print("Inorder  :", tree.inorder(root))
        print("Preorder :", tree.preorder(root))
        print("Postorder:", tree.postorder(root))

    else:
        break