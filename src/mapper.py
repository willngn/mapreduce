class Mapper:
    def __init__(self, input_directory, artist_name, intermediate_file):
        self.input_directory = input_directory
        self.artist_name = artist_name
        self.intermediate_file = intermediate_file

    def map(self):
        # Implement the map task for your specific data processing
        word_count = {}
        with open(self.input_directory, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower()
                    word_count[word] = word_count.get(word, 0) + 1
        for word, count in word_count.items():
            # Write intermediate data to the shared file
            with open(self.intermediate_file, 'a') as int_file:
                int_file.write(f"{self.artist_name}\t{word}\t{count}\n")

# In the main section of the Mapper, you need to pass the shared file:
if __name__ == "__main__":
    # Initialize and run the Mapper for a specific artist
    mapper = Mapper("data/input_data/artist1/song1.txt", "TaylorSwift", "intermediate_data.txt")
    mapper.map()