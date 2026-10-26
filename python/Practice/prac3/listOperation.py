#	Create a list of numbers. Write a Python program to print the sum, average, maximum, and minimum of the numbers.
list = [1,2,3,10,5,26,7]
# sum

summ = 0
for i in list:
    summ = summ + i
print(summ)

# average
avgg = summ/len(list)
print(avgg)

# maximum
maxx = list[0]
for i in list:
    if i > maxx:
        maxx = i 
print(maxx)

#minimun
minn = list[0]

for i in list:
    if i < minn:
        minn = i
print(minn)

# for shortcut
print(sum(list))
print(max(list))
print(min(list))





