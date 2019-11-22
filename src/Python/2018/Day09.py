
# https://adventofcode.com/2018/day/9

#  cyclic intrusive linked list
class LinkedNode:

    def __init__(self, val):
        self.val = val
        self.next = self
        self.prev = self

    def insert(self, val):
        newNode = LinkedNode(val)
        newNode.next = self.next
        newNode.prev = self
        self.next.prev = newNode
        self.next = newNode
        return newNode

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next

    def advance(self, n):
        node = self
        while n > 0:
            node = node.next
            n -= 1
        while n < 0:
            node = node.prev
            n += 1
        return node

    def toArray(self):
        result = [self.val]
        node = self
        while node.next != self:
            node = node.next
            result.append(node.val)
        return result

def play(players, maxScore) :
    scores = [0] * players
    marbles = LinkedNode(0)
    p, m, pos = 0, 1, 0
    while m <= maxScore:
        if m % 23 == 0:
            marbles = marbles.advance(-7)
            scores[p] += m + marbles.val
            marbles = marbles.remove()
        else:
            marbles = marbles.advance(1).insert(m)
        m += 1
        p = (p+1) % players
    return max(scores)

print(play(10, 1618))     # 8317 ?
print(play(13, 7999))     # 146373 ?
print(play(17, 1104))     # 2764 ?
print(play(21, 6111))     # 54718 ?
print(play(30, 5807))     # 37305 ?

from utils import printResult
printResult(1, play(459, 71320))
printResult(2, play(459, 71320 * 100))
