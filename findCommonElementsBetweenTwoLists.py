def common_elements (list1, list2):
    com_elements = []
    for item in list1:
        if item in list2:
            com_elements.append(item)
    return com_elements
lists1=[1,2,3,4,5,6,7]
lists2 = [9,8,7,6,5,4]

com = common_elements(lists2, lists1)
print(com)