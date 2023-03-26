import re


# read a file using generator
def read_with_generator():
    with open('logo.jpg', 'rb') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            yield line


# Define a regular expression to match strings that meet the criteria
regex = rb'\b[a-z]{5,}!(?=[\x00-\x7F]*?\b)'

my_generator = read_with_generator()
matches = []

while True:
    try:
        # read a line from the generator
        binary_line = next(my_generator)

        # Search the binary text that matches the regular expression
        string_matches = re.findall(regex, binary_line)

        # Append the matches to the list of all matches
        matches.extend(string_matches)

    except StopIteration:
        # The generator has finished yielding lines, so exit the loop
        break

# Convert the matches to strings and print them
for match in matches:
    string = match.decode('utf-8')
    print(string)
