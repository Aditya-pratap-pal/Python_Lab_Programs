class queue_implementation:
    def __init__(self, list1=[]):
        self.list1 = list1

    def enqueue(self, n):
        self.list1.append(n)

    def display(self):
        if len(self.list1) == 0:
            print("empty queue")
        else:
            for i in range(len(self.list1) - 1, -1, -1):
                print(self.list1[i], end=" ")
            print("\n")

    def dequeue(self):
        if len(self.list1) == 0:
            print("empty queue")
        else:
            self.list1.pop(0)


class stack_implementation:
    def __init__(self, list1=[]):
        self.list1 = list1

    def push(self, n):
        self.list1.append(n)

    def display_stack(self):
        for i in range(len(self.list1) - 1, -1, -1):
            print(self.list1[i], end=" ")
        print("\n")

    def pop_stack(self):
        if len(self.list1) == 0:
            print("stack is empty")
        else:
            self.list1.pop()


obj1 = stack_implementation()
obj1.push(1)
obj1.display_stack()
obj1.push(2)
obj1.push(3)
obj1.display_stack()
obj1.pop_stack()
obj1.display_stack()

obj2 = queue_implementation()
obj2.enqueue(3)
obj2.enqueue(4)
obj2.enqueue(1)
obj2.enqueue(69)
obj2.display()
obj2.dequeue()
obj2.display()
