from global_variables import *
from mapper import *
from reducer import *
from utils import *
import multiprocessing
reduce_queues = [multiprocessing.Queue() for _ in range(NUM_REDUCERS)]

mapper_processes = []
for i in range(NUM_MAPPERS):
    process = multiprocessing.Process(target=map_task, args=(input, reduce_queues))
    mapper_processes.append(process)
    process.start()

reducer_processes = []
for i in range(NUM_REDUCERS):
    process = multiprocessing.Process(target=reduce_task, args=(reduce_queues[i], f"output/reducer_{i}.txt"))
    reducer_processes.append(process)
    process.start()

for process in mapper_processes:
    process.join()
for process in reducer_processes:
    process.join()

print("MapReduce job completed.")