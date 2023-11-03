class Reducer:
    def __init__(self, intermediate_file, output_directory):
        self.intermediate_file = intermediate_file
        self.output_directory = output_directory

    def reduce(self):
        artist_word_count = {}
        with open(self.intermediate_file, 'r') as int_file:
            for line in int_file:
                artist_name, word, count = line.strip().split('\t')
                count = int(count)
                if artist_name not in artist_word_count:
                    artist_word_count[artist_name] = {}
                if word in artist_word_count[artist_name]:
                    artist_word_count[artist_name][word] += count
                else:
                    artist_word_count[artist_name][word] = count

        for artist_name, word_count in artist_word_count.items():
            output_file = f"{self.output_directory}/{artist_name}.txt"
            with open(output_file, 'w') as file:
                for word, count in word_count.items():
                    file.write(f"{word}: {count}\n")

# In the main section of the Reducer, you need to pass the shared file and output directory:
if __name__ == "__main__":
    # Initialize and run the Reducer for a specific output directory
    reducer = Reducer("intermediate_data.txt", "data/output_data")
    reducer.reduce()