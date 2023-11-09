from global_variables import *
class Reducer:
    def __init__(self, reduce_queue, final_output, output_file):
        self.reduce_queue = reduce_queue
        self.final_output = final_output
        self.output_file = output_file
        self.complete = 0

    def reduce(self):
        while True:
            if self.complete == NUM_MAPPERS:
                break
            item = self.reduce_queue.get()
            if item is None:  # EOF message
                self.complete += 1
            else:
                word, count = item
                self.final_output[word] = self.final_output.get(word, 0) + count
        with open(self.output_file, 'w') as file:
            for word, count in self.final_output.items():
                file.write(f"{word}: {count}\n")