names =[
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat"
        ],
        
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

def count_leaf_items(item_list):
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1

    return count

result = count_leaf_items(names)

print(result)