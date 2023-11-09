from global_variables import *
from mapper import *
from reducer import *
from utils import *
import multiprocessing
import math

def map_task(input, reduce_queues):
    mapper = Mapper(input, reduce_queues)
    mapper.map()

def reduce_task(reduce_queue, final_output, output_file):
    reducer = Reducer(reduce_queue, final_output, output_file)
    reducer.reduce()

def split_text_into_parts(input, num_mapper):
    part_length = math.ceil(len(input) / num_mapper)

    # Split the text into equal parts
    text_parts = [input[i * part_length:(i + 1) * part_length] for i in range(num_mapper)]

    return text_parts

def main():
    reduce_queues = [multiprocessing.Queue() for _ in range(NUM_REDUCERS)]
    print("Read input")
    text_input = read_text_files(INPUT_DIR)
    text_input = split_text_into_parts(text_input, NUM_MAPPERS)
    print("Start reducer processes")
    reducer_processes = []
    for i in range(NUM_REDUCERS):
        process = multiprocessing.Process(target=reduce_task, args=(reduce_queues[i], {}, OUTPUT_FILE))
        reducer_processes.append(process)
        process.start()
    print("Start mapper processes")
    mapper_processes = []
    for i in range(NUM_MAPPERS):
        print(text_input[i])
        process = multiprocessing.Process(target=map_task, args=(text_input[i], reduce_queues))
        mapper_processes.append(process)
        process.start()
    print("Joining")
    for process in mapper_processes:
        process.join()
    for process in reducer_processes:
        process.join()
    print("MapReduce job completed.")
if __name__ == '__main__':
    main()