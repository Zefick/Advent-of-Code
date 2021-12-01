
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/19

input = Input(2020, 19).lines()

class RulesProcessor:

    def __init__(self, rules, part):
        self.part = part
        self.rules = rules.copy()

    def replace(self, rule):
        rule = rule.split()
        result = ""
        for s in rule:
            if s.startswith('"'):
                result = s[1]
            else:
                result += self.processRule(s)
        return result

    def processRule(self, key):
        rule = self.rules[key]
        if rule[0].isdigit() or rule[0] == '"':
            if self.part == 2 and key == '8':
                rule42 = self.processRule('42')
                self.rules[key] = "(" + rule42 + ")+"
            elif self.part == 2 and key == '11':
                rule42 = self.processRule('42')
                rule31 = self.processRule('31')
                self.rules[key] = "(" + rule42 + rule31 \
                        + "|" + rule42 + rule42 + rule31 + rule31 \
                        + "|" + rule42 + rule42 + rule42 + rule31 + rule31 + rule31 \
                        + "|" + rule42 + rule42 + rule42 + rule42 + rule31 + rule31 + rule31 + rule31 \
                        + "|" + rule42 + rule42 + rule42 + rule42 + rule42 + rule31 + rule31 + rule31 + rule31 + rule31 + ")"
                        # looks enough
            else:
                self.rules[key] = "(" + "|".join(map(self.replace, rule.split(" | "))) + ")"

        return self.rules[key]

i = 0
rules = {}
for line in input:
    i += 1
    if len(line) == 0:
        break
    line = line.split(": ")
    rules[line[0]] = line[1]

messages = input[i:]

proc = RulesProcessor(rules, 1)
p = re.compile(proc.processRule("0") + "$")
printResult(1, sum(1 for m in messages if p.match(m)))

proc = RulesProcessor(rules, 2)
p = re.compile(proc.processRule("0") + "$")
printResult(1, sum(1 for m in messages if p.match(m)))
