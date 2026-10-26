# How do you flatten a list of lists into 
# a single list using a list comprehension?

listOfList = [[1,2,3],[4,5,6],[7,8,9]]

lis =[element for sublist in listOfList for element in sublist]
print(lis)