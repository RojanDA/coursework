# wap to find the second largest number in list

def sec_largest(numbers):
    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    print("Largest:", largest)
    print("second largest:", second_largest)
            
numbers = [13,24,56,34,76,57,87,98,76,45]
sec_largest(numbers)


# another process
numbers.sort(reverse=True)
print("Second largest: ",numbers[1])