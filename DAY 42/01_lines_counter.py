# This function can count no of lines in any txt file
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            no_of_lines = len(lines)
        print(f"No. of Lines in {file_path}: {no_of_lines}")
        return no_of_lines
    except FileNotFoundError:
        print("File not Found.")
        return -1
    except Exception as e:
        print(f"An unknow error occured: {e}")
        return -2
    
file_path = r"D:\01_PYTHON\DAY 42\example.txt"
count_lines(file_path)
        