def readlines(input_file):
    # Read each line of text file
    with open(input_file, 'r') as file:
        data = file.read().splitlines()
    return data