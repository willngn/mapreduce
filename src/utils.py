import hashlib
from global_variables import *
import os
import re
def hash(word):
    word = word.encode('utf-8')
    hashed_ver = hashlib.md5(word).hexdigest()
    hash_value = int(hashed_ver, 16)
    return hash_value % NUM_REDUCERS

def read_text_files(input_directory):
    """
    Traverse through all files under the input directory 
    Read all the file content into a single variable
    Assign each line to a mapper based on a round-robin algorithm
    For each line, apply data preprocessing to filter nonalphabetical characters
    Split each line into a list of words, appended to the mapper input list
    Return a list of mapper inputs
    """
    hashset = set()
    mapper_inputs = [[] for _ in range(NUM_MAPPERS)]
    i = 0
    # Recursively traverse the input directory
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".txt") and file_path not in hashset:
                hashset.add(file_path)
                with open(file_path, 'r') as text_file:
                    # Read the content of each text file and append to the result
                    file_content = text_file.read()
                    for line in file_content.splitlines():
                        line = line.translate(TRANSLATION)
                        words = re.split(r'\s+', line.strip())
                        mapper_inputs[i % NUM_MAPPERS] += words
                        i += 1
    return mapper_inputs