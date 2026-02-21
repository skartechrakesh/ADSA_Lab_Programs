class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
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
        new.prev = t

    def delete(self, key):
        t = self.head
        while t:
            if t.data == key:
                if t.prev: t.prev.next = t.next
                else: self.head = t.next
                if t.next: t.next.prev = t.prev
                print("Deleted")
                return
            t = t.next
        print("Not found")

    def forward(self):
        t = self.head
        while t:
            print(t.data, end=" <-> ")
            t = t.next
        print("None")

    def backward(self):
        t = self.head
        if not t: return
        while t.next: t = t.next
        while t:
            print(t.data, end=" <-> ")
            t = t.prev
        print("None")


# ---- default list ----
l = DoublyLinkedList()
for i in [10, 20, 30, 40, 50]:
    l.insert(i)

print("Initial:", end=" "); l.forward()

# ---- menu ----
while True:
    print("\n1.Insert 2.Delete 3.Forward 4.Backward 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        l.insert(int(input("Value: ")))
    elif ch == 2:
        l.delete(int(input("Value: ")))
    elif ch == 3:
        l.forward()
    elif ch == 4:
        l.backward()
    else:
        break