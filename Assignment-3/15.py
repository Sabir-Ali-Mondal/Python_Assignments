def remove_comments(line):
    return line.split('#')[0].strip()

file_path = 'example.py'

with open(file_path, 'r') as file:
    for line in file:
        clean_line = remove_comments(line)
        if clean_line:
            print(clean_line)
