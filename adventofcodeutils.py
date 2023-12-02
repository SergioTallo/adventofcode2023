def readlines(input_file: str) -> list:
    """
    Read each line of text file and return a list of strings containing the lines of input file
    :param input_file: input file to read in string format
    :return: list of strings containing the lines of input file
    """
    # Read each line of text file
    with open(input_file, 'r') as file:
        data = file.read().splitlines()
    return data
