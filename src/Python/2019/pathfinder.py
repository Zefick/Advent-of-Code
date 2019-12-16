
class Pathfinder:

    def __init__(self, step_function, visit_callback = None):
        self.step_function = step_function
        self.visit_callback = visit_callback

    def run(self, start, finish_predicate = None):
        self.visited = {start: 0}
        current = [start]
        step = 0
        while len(current) > 0:
            step += 1
            current = set(filter(lambda x: x not in self.visited,
                    [x for c in current for x in self.step_function(c)]))
            self.visited.update([c, step] for c in current)
            for c in current:
                self.visited[c] = step
                if self.visit_callback:
                    self.visit_callback(c, step)
            if finish_predicate:
                for c in current:
                    if finish_predicate(c):
                        return (c, step)
        return None

    def get_visited(self):
        return self.visited
            
class Pathfinder2D (Pathfinder):

    @staticmethod
    def neighbours(p):
        return [(p[0] + d[0], p[1] + d[1]) for d in [[0, -1], [0, 1], [-1, 0], [1, 0]]]

    def __init__(self, move_check, visit_callback = None):
        super().__init__(
            lambda p: list(filter(move_check, Pathfinder2D.neighbours(p))),
            visit_callback = visit_callback)
