from global_variables import *
import re
class Mapper:
    def __init__(self, input, reducer_queue):
        self.input = input
        self.reducer_queue = reducer_queue

    def map(self):
        output = []
        for line in self.input.splitlines():
            line = line.translate(TRANSLATION)
            words = re.split(r'\s+', line.strip())
            for word in words:
                word = word.lower()
                output.append((word, 1))
        self.reducer_queue.put(output)
        self.reducer_queue.put("EOF")