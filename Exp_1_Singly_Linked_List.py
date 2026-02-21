class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def delete(self, key):
        temp = self.head
        prev = None
        while temp:
            if temp.data == key:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print("Deleted")
                return
            prev = temp
            temp = temp.next
        print("Not found")

    def display(self):
        temp = self.head
        if not temp:
            print("List empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------- Menu --------
l = LinkedList()

while True:
    print("\n1.Insert \n2.Delete \n3.Display \n4.Exit\n")
    ch = int(input("Choice: "))

    if ch == 1:
        l.insert(int(input("Enter value: ")))
    elif ch == 2:
        l.delete(int(input("Enter value: ")))
    elif ch == 3:
        l.display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")
