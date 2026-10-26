#Write a program to count the number of vowels in a given string.

def count_vowels(string): 
  vowels = "aeiouAEIOU"
  count = 0
  for char in string:
    if char in vowels:
      count += 1

  return count



x = input("enter a string: ")

num = count_vowels(x)

print("number of vowels:", num)
