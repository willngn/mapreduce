from global_variables import *
import re
from utils import *
class Mapper:
    def __init__(self, input, reduce_queues):
        self.input = input
        self.reduce_queues = reduce_queues

    def map(self):
        for line in self.input.splitlines():
            line = line.translate(TRANSLATION)
            words = re.split(r'\s+', line.strip())
            for word in words:
                word = word.lower()
                reducer_idx = hash(word) % NUM_REDUCERS
                self.reduce_queues[reducer_idx].put((word, 1))
        for queue in self.reduce_queues:
            queue.put(None) # EOF message