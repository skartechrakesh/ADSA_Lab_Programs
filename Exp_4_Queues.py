class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if not self.q:
            print("Queue Underflow")
        else:
            print("Removed:", self.q.pop(0))

    def peek(self):
        if not self.q:
            print("Queue Empty")
        else:
            print("Front:", self.q[0])

    def display(self):
        if not self.q:
            print("Queue Empty")
        else:
            print("Queue:", self.q)


# -------- Menu --------
qu = Queue()

while True:
    print("\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        qu.enqueue(int(input("Enter value: ")))
    elif ch == 2:
        qu.dequeue()
    elif ch == 3:
        qu.peek()
    elif ch == 4:
        qu.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
