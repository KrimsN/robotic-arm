import numpy.random as random
from copy import deepcopy


class SimpleACO:
    def __init__(self, G, end, decay):
        random.seed()
        self.graph = G
        self.end = end
        self.rate = decay
        self.ants = None
        self.proto_ant = None

    def make_ants(self, amount):
        if self.proto_ant is None:
            raise TypeError('No ant specified')

        self.ants = [deepcopy(self.proto_ant) for i in range(amount)]

    def generate_solutions(self):
        lens = []
        for i, a in enumerate(self.ants):
            print('Ant #', i + 1)
            while a.pos != self.end:
                a.pick_edge()
            a.remove_cycles()
            length = a.path_len
            lens.append(length)
            print('Ant #', i + 1, 'finished, length:', length)
        return min(lens), max(lens), sum(lens) / len(lens)

    def set_proto(self, p):
        self.proto_ant = p

    def update_pheromone(self):
        # испарение
        self.graph.evaporate(self.rate)
        # отложение
        for a in self.ants:
            a.deposit_pheromone()
            a.unwind_path()

    def daemon_actions(self):
        pass