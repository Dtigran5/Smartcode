def count(lst):
    result = []
    count = 1

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            result.append(count)
            count = 1
    result.append(count)  

    return result

mylist = [
    [1, 1, 1, 2, 2, 4, 2, 2, 3, 1, 1, 4, 4]
]

for _ in range(5):  
    new_list = count(mylist[-1])
    mylist.append(new_list)

for lst in mylist:
    print(lst)
