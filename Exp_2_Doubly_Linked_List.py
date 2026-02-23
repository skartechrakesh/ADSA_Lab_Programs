class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ---------- INSERTION ----------
    def insert_begin(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        new.next = self.head
        self.head.prev = new
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = new
        new.prev = t

    def insert_pos(self, data, pos):
        new = Node(data)
        if pos == 1:
            self.insert_begin(data)
            return
        t = self.head
        for i in range(pos - 2):
            if not t:
                print("Invalid Position")
                return
            t = t.next
        if not t:
            print("Invalid Position")
            return
        new.next = t.next
        new.prev = t
        if t.next:
            t.next.prev = new
        t.next = new

    # ---------- DELETION ----------
    def delete_begin(self):
        if not self.head:
            print("List Empty")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
        if not self.head:
            print("List Empty")
            return
        t = self.head
        if not t.next:
            self.head = None
            return
        while t.next:
            t = t.next
        t.prev.next = None

    def delete_pos(self, pos):
        if not self.head:
            print("List Empty")
            return
        if pos == 1:
            self.delete_begin()
            return
        t = self.head
        for i in range(pos - 1):
            if not t:
                print("Invalid Position")
                return
            t = t.next
        if not t:
            print("Invalid Position")
            return
        if t.next:
            t.next.prev = t.prev
        if t.prev:
            t.prev.next = t.next

    # ---------- TRAVERSAL ----------
    def forward(self):
        t = self.head
        while t:
            print(t.data, end=" <-> ")
            t = t.next
        print("None")

    def backward(self):
        t = self.head
        if not t:
            return
        while t.next:
            t = t.next
        while t:
            print(t.data, end=" <-> ")
            t = t.prev
        print("None")


# --------- INITIAL LIST CREATION ---------
l = DoublyLinkedList()

for i in [10, 20, 30, 40, 50]:
    l.insert_end(i)

print("Initial Doubly Linked List (Forward):")
l.forward()

# --------- MENU ---------
while True:
    print("\n1.Insert Begin 2.Insert End 3.Insert Position")
    print("4.Delete Begin 5.Delete End 6.Delete Position")
    print("7.Forward 8.Backward 9.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        l.insert_begin(int(input("Value: ")))

    elif ch == 2:
        l.insert_end(int(input("Value: ")))

    elif ch == 3:
        val = int(input("Value: "))
        pos = int(input("Position: "))
        l.insert_pos(val, pos)

    elif ch == 4:
        l.delete_begin()

    elif ch == 5:
        l.delete_end()

    elif ch == 6:
        pos = int(input("Position: "))
        l.delete_pos(pos)

    elif ch == 7:
        l.forward()

    elif ch == 8:
        l.backward()

    else:
        break