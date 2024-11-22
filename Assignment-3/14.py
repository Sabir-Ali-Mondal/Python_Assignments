source_file = 'source.txt'
destination_file = 'destination.txt'

with open(source_file, 'r') as src:
    content = src.read()

with open(destination_file, 'w') as dest:
    dest.write(content)
