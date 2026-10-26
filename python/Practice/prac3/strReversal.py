# o	Write a Python function to reverse a given string.

str = "Rojan Chandra Poudel"
revStr = ""
for i in str:
   revStr = i + revStr 
print(revStr.title())

# another process
def revStr(s):
   rev_s = ''

   for char in reversed(s):
      rev_s += char

   return rev_s
str = input("enter a string you want to reversed: ")

revStr = revStr(str)
print(revStr)
