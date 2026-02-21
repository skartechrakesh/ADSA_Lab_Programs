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
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = new

    def delete(self, key):
        t, prev = self.head, None
        while t:
            if t.data == key:
                if prev: prev.next = t.next
                else: self.head = t.next
                print("Deleted")
                return
            prev, t = t, t.next
        print("Not found")

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next
        print("None")


# ---- default list ----
l = LinkedList()
for i in [10, 20, 30, 40, 50]:
    l.insert(i)

print("Initial:", end=" "); l.display()

# ---- menu ----
while True:
    print("\n1.Insert 2.Delete 3.Display 4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        l.insert(int(input("Value: ")))
    elif ch == 2:
        l.delete(int(input("Value: ")))
    elif ch == 3:
        l.display()
    else:
        break