# How do you sort a list of tuples based on 
# the second element of each tuple?

list_of_tuples = [(1, 'c'), (2, 'a'), (3, 'b')]

sorted_list = sorted(list_of_tuples, key=lambda x: x[1])

print(sorted_list)