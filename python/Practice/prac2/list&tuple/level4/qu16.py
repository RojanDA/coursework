# How do you remove duplicate elements from 
# a list while preserving the order?

def rev_dup(n):
    seen = set()
    result = []
    for item in n:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# using list comprehension
def rev_dup_com(n):
    seen = set()
    return [x for x in n if not(x in seen or seen.add(x))]



n = [1,1,2,3,3,4,5,5,6,7,7,8,8,9,9]
n1 = rev_dup(n)
n2 = rev_dup(n)
print(n1)
print(n2)