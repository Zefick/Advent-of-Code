
from utils import Input, printResult

# https://adventofcode.com/2020/day/23

input = "158937462"

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def drop_next(self):
        next = self.next
        self.next = self.next.next
        return next

    def insert_next(self, node):
        node.next = self.next
        self.next = node

def play(cups, moves):
    arr = list(map(int, input))
    m = max(arr)
    arr += list(range(m+1, cups+1))

    cur_node = Node(arr[0])
    nodes = {cur_node.val: cur_node}
    head = cur_node
    for val in arr[1:]:
        node = Node(val)
        nodes[val] = node
        cur_node.next = node
        cur_node = node
    cur_node.next = head
    cur_node = head

    for n in range(moves):
        a = cur_node.next
        b = a.next
        c = b.next
        cur_node.next = c.next
        j = cur_node.val - 1
        while j == 0 or j == a.val or j == b.val or j == c.val:
            j -= 1
            if j <= 0:
                j = cups
        dest = nodes[j]
        c.next = dest.next
        dest.next = a
        cur_node = cur_node.next
        
        # if n % 1000000 == 0:
        #     print(n)

    return nodes[1]

one = play(9, 100)
s = []
node = one.next
while node != one:
    s.append(node.val)
    node = node.next
printResult(1, "".join(map(str, s)))

import time
t = time.time()

one = play(1000000, 10**7)
x, y = one.next.val, one.next.next.val
printResult(2, x * y)

# print(time.time() - t)
