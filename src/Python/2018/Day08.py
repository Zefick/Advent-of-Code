
from utils import Input, printResult

# https://adventofcode.com/2018/day/8

class Node:

    def __init__(self, nums, index):
        n, m = nums[index : index+2]
        self.children = []
        k = index + 2
        for i in range(n):
            child = Node(nums, k)
            k += child.length
            self.children.append(child)
        self.length = k - index + m
        self.meta = nums[k : k+m]

    def part1(self):
        return sum(self.meta) + sum(map(Node.part1, self.children))

    def part2(self):
        l = len(self.children)
        if l == 0:
            return sum(self.meta)
        else:
            return sum(self.children[i-1].part2() for i in self.meta if i <= l)

nums = list(map(int, Input(2018, 8).lines()[0].split(" ")))
root = Node(nums, 0)
printResult(1, root.part1())
printResult(2, root.part2())
