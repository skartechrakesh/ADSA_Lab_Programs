class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    # Delete node
    def delete(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                print("Deleted")
                return
            temp = temp.next
        print("Not found")

    # Forward traversal
    def forward(self):
        temp = self.head
        if not temp:
            print("List empty")
            return
        while temp:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")

    # Backward traversal
    def backward(self):
        temp = self.head
        if not temp:
            print("List empty")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# -------- Menu --------
l = DoublyLinkedList()

while True:
    print("\n1.Insert \n2.Delete \n3.Forward \n4.Backward \n5.Exit\n")
    ch = int(input("Choice: "))

    if ch == 1:
        l.insert(int(input("Enter value: ")))
    elif ch == 2:
        l.delete(int(input("Enter value: ")))
    elif ch == 3:
        l.forward()
    elif ch == 4:
        l.backward()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
