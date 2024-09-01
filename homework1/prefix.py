mylist1 = ['flower', 'flow', 'flight']
prefixes = set()

for word in mylist1:
    for i in range(1, len(word) + 1):
        prefixes.add(word[:i])

print(prefixes)

