# https://www.acmicpc.net/problem/10845
import sys


class Queue:
    pointer = 0
    list = []

    def size(self):
        start = self.pointer
        end = len(self.list)
        return len(self.list[start:end])

    def empty(self):
        if self.pointer != len(self.list):
            return 0

        return 1

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.empty():
            return -1

        value = self.list[self.pointer]
        self.pointer += 1

        return value

    def front(self):
        if self.empty():
            return -1

        return self.list[self.pointer]

    def back(self):
        if self.empty():
            return -1

        return self.list[-1]


queue = Queue()

for i in range(int(input())):
    command, *value = sys.stdin.readline().split()
    value = None if not value else value[0]

    fn = getattr(queue, command)

    if command.lower() == "push":
        fn(value)
    else:
        print(fn())
