import sys


class Stack:
    list = []

    def size(self):
        return len(self.list)

    def empty(self):
        if not self.list:
            return 1

        return 0

    def top(self):
        if self.empty():
            return -1

        return self.list[-1]

    def push(self, number):
        self.list.append(number)

    def pop(self):
        if self.empty():
            return -1

        return self.list.pop()


count = int(input())
stack = Stack()

for i in range(count):
    data = sys.stdin.readline().split()

    if not data:
        break

    fn = getattr(stack, data[0])

    if len(data) > 1:
        value = int(data[1])
        fn(value)
    else:
        print(fn())
