def sum_of_all_items(data):
    if isinstance(data, dict):
        return sum(data.values())
    elif isinstance(data, (set, tuple, list)):
        return sum(data)
    else:
        raise TypeError("Unsupported data type")

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_set = {1, 2, 3}
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

print("Sum of dictionary values:", sum_of_all_items(my_dict))
print("Sum of set items:", sum_of_all_items(my_set))
print("Sum of tuple items:", sum_of_all_items(my_tuple))
print("Sum of list items:", sum_of_all_items(my_list))