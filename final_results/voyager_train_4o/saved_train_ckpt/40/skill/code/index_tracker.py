

def index_tracker(int_list):
    index_dict = {}
    for (index, value) in enumerate(int_list):
        if (value not in index_dict):
            index_dict[value] = []
        index_dict[value].append(index)
    return index_dict
