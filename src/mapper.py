from global_variables import *
from utils import hash
class Mapper:
    def __init__(self, input, reduce_queues):
        # the input is a list of words
        self.input = input
        # a list of reducer queues
        self.reduce_queues = reduce_queues

    def map(self):
        for word in self.input:
            word = word.lower()
            if len(word) > 1 and word.isalpha():
                reducer_idx = hash(word) % NUM_REDUCERS
                self.reduce_queues[reducer_idx].put((word, 1))
        for queue in self.reduce_queues:
            queue.put(None) # EOF message