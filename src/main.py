from global_variables import *
from mapper import *
from reducer import *
from utils import *
import multiprocessing
from time import time
import random
def map_task(input, reduce_queues):
    mapper = Mapper(input, reduce_queues)
    mapper.map()

def reduce_task(reduce_queue, final_output, output_file):
    reducer = Reducer(reduce_queue, final_output, output_file)
    reducer.reduce()

def main(kill=False):
    start = time()
    reduce_queues = [multiprocessing.Queue() for _ in range(NUM_REDUCERS)]
    print("Read input and assign to mapper")
    input = read_text_files(INPUT_DIR)
    read = time() - start
    print(f"Reading files takes: {read} seconds")
    print("Start reducer processes")
    reducer_processes = []
    for i in range(NUM_REDUCERS):
        process = multiprocessing.Process(target=reduce_task, args=(reduce_queues[i], {}, OUTPUT_FILE))
        reducer_processes.append(process)
        process.start()
    print("Start mapper processes")
    mapper_processes = []
    for i in range(NUM_MAPPERS):
        process = multiprocessing.Process(target=map_task, args=(input[i], reduce_queues))
        mapper_processes.append(process)
        process.start()
    if kill:
        phase = random.randint(0, 1)
        if phase == 0:
            idx = random.randint(0, NUM_MAPPERS - 1)
            print(f"Mapper {idx} is terminated")
            mapper_processes[idx].terminate()
        else:
            idx = random.randint(0, NUM_REDUCERS - 1)
            print(f"Reducer {idx} is terminated")
            reducer_processes[idx].terminate()
    print("Joining mapper")
    for process in mapper_processes:
        process.join()
    map = time() - start - read
    print(f"It takes {map / 60} minutes to finish mapping since reading all files")
    print("Joining reducer")
    for process in reducer_processes:
        process.join()
    reduce = time() - start - read
    print(f"It takes {reduce / 60} minutes to finish reducing since reading all files")
    print("MapReduce job completed.")
if __name__ == '__main__':
    main(kill=False)