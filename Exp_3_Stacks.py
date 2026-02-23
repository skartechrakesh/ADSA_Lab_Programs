class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        if not self.s:
            print("Stack Underflow")
        else:
            print("Popped:", self.s.pop())

    def peek(self):
        if not self.s:
            print("Stack Empty")
        else:
            print("Top:", self.s[-1])

    def display(self):
        if not self.s:
            print("Stack Empty")
        else:
            print("Stack:", self.s[::-1])   # top to bottom


# -------- Menu --------
st = Stack()

while True:
    print("\n1.Push 2.Pop 3.Peek 4.Display 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        st.push(int(input("Enter value: ")))
    elif ch == 2:
        st.pop()
    elif ch == 3:
        st.peek()
    elif ch == 4:
        st.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
