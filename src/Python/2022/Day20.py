
from utils import Input, printResult

# https://adventofcode.com/2022/day/20

input = list(map(int, Input(2022, 20).lines()))

class ListNode:
    
    def __init__(self, val, prev=None):
         self.prev = prev
         self.next = None
         self.val = val
         if prev:
            prev.next = self

    def move_forvard(self, n):
        if n > 0:
            next = self
            for _ in range(n):
                next = next.next
                
            self.next.prev = self.prev
            self.prev.next = self.next
            self.next, self.prev = next.next, next
            next.next.prev = next.next = self
          
def find_node(node, x):
    while True:
        if node.val == x:
            return node
        node = node.next

head = None
prev = None
nodes = []
for x in input:
    node = ListNode(x, prev)
    if not head:
        head = node
    prev = node
    nodes.append(node)
node.next = head
head.prev = node

for node in nodes:
    node.move_forvard(node.val % (len(input) - 1))

node = find_node(head, 0)
res = []
for _ in range(3):
    for _ in range(1000):
        node = node.next
    res.append(node.val)
    
printResult(1, sum(res))

# part 2

key = 811589153
head = None
prev = None
nodes = []
for x in input:
    node = ListNode(x * key ,prev)
    if not head:
        head = node
    prev = node
    nodes.append(node)
node.next = head
head.prev = node

for i in range(10):
    # print(i)
    for node in nodes:
        node.move_forvard(node.val % (len(input) - 1))
        
node = find_node(head, 0)
res = []
for _ in range(3):
    for _ in range(1000):
        node = node.next
    res.append(node.val)
    
printResult(2, sum(res))
