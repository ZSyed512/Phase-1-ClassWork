import csv


class StockData:
    def __init__(self, filename):
        self.filename = filename
        self.data = []class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        raise NotImplementedError("Subclasses must implement this method")

class Preprocessor(DataProcessor):
    def process(self):
        # Implement preprocessing steps
        print("Data preprocessing done.")

class ModelTrainer(DataProcessor):
    def process(self):
        # Implement model training steps
        print("Model training done.")

class DataSciencePipeline:
    def __init__(self, data):
        self.data = data
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run_pipeline(self):
        for step in self.steps:
            step.process()

# Example usage
data = [1, 2, 3, 4, 5]

pipeline = DataSciencePipeline(data)
pipeline.add_step(Preprocessor(data))
pipeline.add_step(ModelTrainer(data))

pipeline.run_pipelineclass DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        raise NotImplementedError("Subclasses must implement this method")

class Preprocessor(DataProcessor):
    def process(self):
        # Implement preprocessing steps
        print("Data preprocessing done.")

class ModelTrainer(DataProcessor):
    def process(self):
        # Implement model training steps
        print("Model training done.")

class DataSciencePipeline:
    def __init__(self, data):
        self.data = data
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run_pipeline(self):
        for step in self.steps:
            step.process()

# Example usage
data = [1, 2, 3, 4, 5]

pipeline = DataSciencePipeline(data)
pipeline.add_step(Preprocessor(data))
pipeline.add_step(ModelTrainer(data))

pipeline.run_pipelineclass DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        raise NotImplementedError("Subclasses must implement this method")

class Preprocessor(DataProcessor):
    def process(self):
        # Implement preprocessing steps
        print("Data preprocessing done.")

class ModelTrainer(DataProcessor):
    def process(self):
        # Implement model training steps
        print("Model training done.")

class DataSciencePipeline:
    def __init__(self, data):
        self.data = data
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run_pipeline(self):
        for step in self.steps:
            step.process()

# Example usage
data = [1, 2, 3, 4, 5]

pipeline = DataSciencePipeline(data)
pipeline.add_step(Preprocessor(data))
pipeline.add_step(ModelTrainer(data))

pipeline.run_pipeline
class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        raise NotImplementedError("Subclasses must implement this method")

class Preprocessor(DataProcessor):
    def process(self):
        # Implement preprocessing steps
        print("Data preprocessing done.")

class ModelTrainer(DataProcessor):
    def process(self):
        # Implement model training steps
        print("Model training done.")

class DataSciencePipeline:
    def __init__(self, data):
        self.data = data
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run_pipeline(self):
        for step in self.steps:
            step.process()

# Example usage
data = [1, 2, 3, 4, 5]

pipeline = DataSciencePipeline(data)
pipeline.add_step(Preprocessor(data))
pipeline.add_step(ModelTrainer(data))

pipeline.run_pipeline
    def read_csv(self):
        with open(self.filename, 'r') as file:
            # TODO: Use the csv.reader function to read the contents of the file
            reader = csv.reader(file) # Replace None with appropriate code

            # TODO: Skip the header of the CSV file
            next(reader)

            for row in reader:
                self.data.append(row)

    def calculate_lengths(self):
        lengths = []
        for row in self.data:
            # TODO: Count the number of non-empty items in each row
            # and append the count to the lengths list
            # also be sure to ignore the date value in this list
            length = None  # Replace None with appropriate code
            lengths.append(length)
        return lengths


# Part 2: Instantiate the StockData class and call its methods
# TODO: Create an instance of StockData with the filename 'stock_data.csv
StockData(filename = "stock_data.csv")

# TODO: Call the read_csv method of the instance
#

# TODO: Print the data attribute of the instance
...

# TODO: Call the calculate_lengths method and print the result
...
