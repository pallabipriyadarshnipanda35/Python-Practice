def add_value(dictionary, key, value):
    dictionary[key] = value
    return dictionary

def delete_value(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

def discard_value(dictionary, key):
    dictionary.pop(key, None)
    return dictionary

def update_value(dictionary, key, value):
    if key in dictionary:
        dictionary[key] = value
    return dictionary

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Add value
my_dict = add_value(my_dict, 'd', 4)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Delete value
my_dict = delete_value(my_dict, 'b')
print(my_dict)  # {'a': 1, 'c': 3, 'd': 4}

# Discard value
my_dict = discard_value(my_dict, 'c')
print(my_dict)  # {'a': 1, 'd': 4}

# Update value
my_dict = update_value(my_dict, 'a', 10)
print(my_dict)  # {'a': 10, 'd': 4}