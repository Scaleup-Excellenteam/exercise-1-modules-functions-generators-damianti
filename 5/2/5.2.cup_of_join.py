# Function to join multiple lists with a specified separator.
def join(*lists, sep='-'):
    # Return None if no lists are provided.
    if not lists:
        return None

    result = []

    # Iterate through the input lists.
    for i, lst in enumerate(lists):
        # Add the separator between the lists, but not before the first list.
        if i > 0:
            result.append(sep)
        # Extend the result list with the elements from the current list.
        result.extend(lst)

    return result


list1 = ["hello", "world"]
list2 = ["how", "are", "you"]
list3 = ["today", "?"]

# Test the join function with the default separator.
print(join(list1, list2, list3))  # Output: ['hello', 'world', '-', 'how', 'are', 'you', '-', 'today', '?']

# Test the join function with a custom separator.
print(join(list1, list2, list3, sep="@"))  # Output: ['hello', 'world', '@', 'how', 'are', 'you', '@', 'today', '?']

# Test the join function with a single list.
print(join([1]))  # Output: [1]

# Test the join function with no input lists.
print(join())  # Output: None
