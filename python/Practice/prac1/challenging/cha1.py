#  Write a program that removes all duplicate characters from a string.

def rev_dup(in_str):
    seen = set()
    result = []

    for char in in_str:
        if char not in seen :
            seen.add(char)
            result.append(char)
    
    return ' '.join(result)

in_str = input("enter a string: ")
out_str = rev_dup(in_str)
print(f"string after removing duplicates: {out_str}")