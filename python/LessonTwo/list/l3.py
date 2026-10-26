# wap to remove duplisates from a list


def remove_duplicates(lst):
    return list(set(lst))

list1 = ["rojan","poudel","chandra","hero","smart","rojan","chandra","hero"]
unique_list = remove_duplicates(list1)
print("list affter removing duolicates:",unique_list)
