import string
NUM_MAPPERS = 3
NUM_REDUCERS = 3
# !"#$%&()*+,-./:;<=>?@[\]^_`{|}~
# still preserve single quotes to account for isn't or didn't words
TRANSLATION = str.maketrans(string.punctuation.replace("'", ""), ' ' * len(string.punctuation.replace("'", "")))
