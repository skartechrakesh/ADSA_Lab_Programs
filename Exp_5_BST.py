class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


class BST:
    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if not root:
            print("Not Found")
        elif root.key == key:
            print("Found")
        elif key < root.key:
            self.search(root.left, key)
        else:
            self.search(root.right, key)

    def minValue(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = self.minValue(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    # Traversals
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# -------- Menu --------
tree = BST()
root = None

while True:
    print("\n1.Insert \n2.Delete \n3.Search \n4.Inorder \n5.Preorder \n6.Postorder \n7.Exit\n")
    ch = int(input("Choice: "))

    if ch == 1:
        root = tree.insert(root, int(input("Enter value: ")))
    elif ch == 2:
        root = tree.delete(root, int(input("Enter value: ")))
    elif ch == 3:
        tree.search(root, int(input("Enter value: ")))
    elif ch == 4:
        tree.inorder(root); print()
    elif ch == 5:
        tree.preorder(root); print()
    elif ch == 6:
        tree.postorder(root); print()
    elif ch == 7:
        break
    else:
        print("Invalid choice")
