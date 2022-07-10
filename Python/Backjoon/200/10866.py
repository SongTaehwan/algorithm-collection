# https://www.acmicpc.net/problem/10866
import sys


class Deque:
    list = []

    def size(self):
        return len(self.list)

    def empty(self):
        if self.size() != 0:
            return 0
        return 1

    def push_back(self, value):
        self.list.append(value)

    def push_front(self, value):
        self.list = [value] + self.list

    def pop_back(self):
        if self.empty():
            return -1

        return self.list.pop()

    def pop_front(self):
        if self.empty():
            return -1

        return self.list.pop(0)

    def front(self):
        if self.empty():
            return -1

        return self.list[0]

    def back(self):
        if self.empty():
            return -1

        return self.list[-1]


deque = Deque()

for i in range(int(sys.stdin.readline())):
    command, *value = sys.stdin.readline().split()
    value = value[0] if value else None

    fn = getattr(deque, command)

    if command.lower().count("push"):
        fn(value)
    else:
        print(fn())
