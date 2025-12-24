def build_dict_from_list(List):
    new_dict = [None] * len(List)
    for item in List:
        hash_val = hash(item) % len(new_dict)
        slot = hash_val
        new_dict[slot] = item
    return new_dict

Dict = build_dict_from_list(list(range(0,101)))