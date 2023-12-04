def element_at(my_list, idx):
    if idx in range(len(my_list)):
        return my_list[idx]
    else:
        return None
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 13
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
