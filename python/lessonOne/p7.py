# wap to find the largest element in a list

list = [12,23,43,56,76,89,33]
largest = list[0]
smallest = list[0]
for num in list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print(largest)
print(smallest)
