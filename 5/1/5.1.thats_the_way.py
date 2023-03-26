import os


# Function to find and return files starting with a specific prefix in a given directory.
def prefix_url(url='images', prefix='deep'):
    files = []

    # Iterate through the files in the given directory.
    for file in os.listdir(url):

        if file.startswith(prefix):
            files.append(file)

    return files


# Call the prefix_url function and print the result.
print(prefix_url())
