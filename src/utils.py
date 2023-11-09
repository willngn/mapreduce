import hashlib
from global_variables import *
from mapper import *
from reducer import *
import os 

def hash(word):
    word = word.encode('utf-8')
    hashed_ver = hashlib.md5(word).hexdigest()
    hash_value = int(hashed_ver, 16)
    return hash_value % NUM_REDUCERS

def read_text_files(input_directory):
    all_text = ""
    hashset = set()
    # Recursively traverse the input directory
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".txt") and file_path not in hashset:
                hashset.add(file_path)
                with open(file_path, 'r') as text_file:
                    # Read the content of each text file and append to the result
                    file_content = text_file.read()
                    all_text += file_content
    return all_text
print(read_text_files(INPUT_DIR))


def map_task(input, reduce_queues):
    mapper = Mapper(input, reduce_queues)
    mapper.map()

def reduce_task(reduce_queue, final_output, output_file=OUTPUT_FILE):
    reducer = Reducer(reduce_queue, final_output, output_file)
    reducer.reduce()