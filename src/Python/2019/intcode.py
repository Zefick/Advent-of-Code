
class Intcode:

    def __init__(self, ram):
        self.ram = list(ram) + [0] * 10000

    def run(self, input):
        ram = self.ram
        ptr = 0
        shifts = {1:4, 2:4, 3:2, 4:2, 7:4, 8:4, 9:2}
        base = 0
        dataPtr = 0
        while ram[ptr] != 99:
            code = ram[ptr]
            op = code % 100

            a = ram[ptr+1]
            if code // 100 % 10 == 1:
                a = ptr + 1
            elif code // 100 % 10 == 2:
                a = a + base

            if op in [1, 2, 5, 6, 7, 8]:
                b = ram[ptr + 2]
                if code // 1000 % 10 == 1:
                    b = ptr + 2
                elif code // 1000 % 10 == 2:
                    b = b + base

            if op in [1, 2, 7, 8]:
                c = ram[ptr + 3]
                if code // 10000 % 10 == 1:
                    c = ptr + 3
                elif code // 10000 % 10 == 2:
                    c = c + base

            if op == 1:
                ram[c] = ram[a] + ram[b]
            elif op == 2:
                ram[c] = ram[a] * ram[b]
            elif op == 3:
                while dataPtr >= len(input):
                    yield "wait"
                ram[a] = input[dataPtr]
                dataPtr += 1
            elif op == 4:
                yield ram[a]
            elif op == 5:
                ptr = ram[b] if ram[a] != 0 else ptr + 3
            elif op == 6:
                ptr = ram[b] if ram[a] == 0 else ptr + 3
            elif op == 7:
                ram[c] = int(ram[a] < ram[b])
            elif op == 8:
                ram[c] = int(ram[a] == ram[b])
            elif op == 9:
                base += ram[a]
            ptr += shifts.get(op, 0)
        return

