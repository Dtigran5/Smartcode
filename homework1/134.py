def generate_sublists(input_list):
    sublists = [[]]
    for i in range(len(input_list)):
        sublists += [current + [input_list[i]] for current in sublists]
    return sublists

test_lists = [[1, 2, 3], ['a', 'b'], [True, False]]
for ls in test_lists:
    print(f"Sublists of {ls}: {generate_sublists(ls)}")
    
