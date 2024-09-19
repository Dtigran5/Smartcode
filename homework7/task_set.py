#1
my_set = {1, 2, 3, 4, 5}
print(my_set)

#2
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

#3
my_set = set()
my_set.add("Member1")
my_set.update(["Member2", "Member3", "Member4"])
print(my_set)

#4
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
my_set.difference_update({1, 2})
print(my_set)

#5
my_set = {1, 2, 3, 4, 5}
item_to_remove = 3
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
print(my_set)

#6
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
intersection = set_a.intersection(set_b)
print("Intersection of sets:", intersection)

#7
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_set = set_a.union(set_b)
print("Union of sets:", union_set)

#8
set_a = {1, 2, 3}
set_b = {1, 2}
is_subset = set_b.issubset(set_a)
print(f"Is set_b a subset of set_a? {is_subset}")
is_superset = set_a.issuperset(set_b)
print(f"Is set_a a superset of set_b? {is_superset}")

#9
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set) 

#10
def find_max_min(values):
    maximum = max(values)
    minimum = min(values)
    return maximum, minimum

my_set = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}
max_value, min_value = find_max_min(my_set)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

#11
my_set = {1, 2, 3, 4, 5}
length_of_set = len(my_set)
print("The length of the set is:", length_of_set)
