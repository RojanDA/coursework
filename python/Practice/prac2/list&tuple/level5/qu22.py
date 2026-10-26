# How do you use the filter function to
# filter out even numbers from a list?


num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

fliNum = list(filter(lambda x: x% 2 != 0, num))
print(fliNum)