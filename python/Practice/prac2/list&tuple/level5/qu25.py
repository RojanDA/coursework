# How do you create a tuple of lists and modify 
# the lists within the tuple?

tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'], [True, False])

tuple_of_lists[1].append('d')

print(tuple_of_lists)
