import string
NUM_MAPPERS = 2
NUM_REDUCERS = 2
# !"#$%&()*+,-./:;<=>?@[\]^_`{|}~
# still preserve single quotes to account for isn't or didn't words
TRANSLATION = str.maketrans(string.punctuation.replace("'", ""), ' ' * len(string.punctuation.replace("'", "")))
INPUT_DIR = "data/input"
OUTPUT_FILE = "data/output.txt"