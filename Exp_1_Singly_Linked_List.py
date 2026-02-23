class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # ---------- INSERTION ----------
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
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

    def insert_pos(self, data, pos):
        new = Node(data)
        if pos == 1:
            new.next = self.head
            self.head = new
            return

        t = self.head
        for i in range(pos - 2):
            if not t:
                print("Invalid Position")
                return
            t = t.next

        new.next = t.next
        t.next = new

    # ---------- DELETION ----------
    def delete_begin(self):
        if not self.head:
            print("List Empty")
            return
        self.head = self.head.next

    def delete_end(self):
        if not self.head:
            print("List Empty")
            return
        if not self.head.next:
            self.head = None
            return
        t = self.head
        while t.next.next:
            t = t.next
        t.next = None

    def delete_pos(self, pos):
        if not self.head:
            print("List Empty")
            return
        if pos == 1:
            self.head = self.head.next
            return

        t = self.head
        for i in range(pos - 2):
            if not t.next:
                print("Invalid Position")
                return
            t = t.next

        if not t.next:
            print("Invalid Position")
            return

        t.next = t.next.next

    # ---------- DISPLAY ----------
    def display(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next
        print("None")


# --------- INITIAL LIST CREATION ---------
l = LinkedList()

# Creating list initially in the code
for i in [10, 20, 30, 40, 50]:
    l.insert_end(i)

print("Initial Linked List:")
l.display()

# --------- MENU ---------
while True:
    print("\n1.Insert Begin 2.Insert End 3.Insert Position")
    print("4.Delete Begin 5.Delete End 6.Delete Position")
    print("7.Display 8.Exit")

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
        l.display()

    else:
        break