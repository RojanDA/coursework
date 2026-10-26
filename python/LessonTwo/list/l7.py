# wap to sort a list of numbers in ascending a desending order

def assending(lst):
    return sorted(lst)

def desending(lst):
    return sorted(lst, reverse = True)

list = [7,9,6,1,8,2,3,18,16,4,21,5,26]

ass = assending(list)
des = desending(list)
print(ass)
print(des)