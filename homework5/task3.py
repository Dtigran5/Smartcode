def stem_and_leaf(data):
    stem_leaf_dict = {}
    
    for number in data:
        stem = number // 10
        leaf = number % 10
        
        if stem not in stem_leaf_dict:
            stem_leaf_dict[stem] = []
        
        stem_leaf_dict[stem].append(leaf)
    
    for key in stem_leaf_dict:
        stem_leaf_dict[key].sort()
    
    return stem_leaf_dict

data = [11, 35, 14, 9, 39, 23, 35]
print(stem_and_leaf(data))
