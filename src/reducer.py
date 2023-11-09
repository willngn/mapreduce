from global_variables import *
class Reducer:
    def __init__(self, mapper_output, result_queue):
        self.mapper_output = mapper_output
        self.result_queue = result_queue
        self.complete = 0

    def reduce(self):
        counter = {}
        while True:
            if self.complete == NUM_MAPPERS:
                break
            item = self.reducer_queue.get()
            if item is None:  # EOF message
                self.complete += 1
            word, count = item
            counter[word] = counter.get(word, 0) + count
        self.result_queue.put(counter)