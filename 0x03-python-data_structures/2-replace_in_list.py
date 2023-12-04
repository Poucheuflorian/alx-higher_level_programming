def replace_in_list(my_list, idx, element):
    new_list =  my_list.copy()
    if( idx  in range(len(my_list))):
        new_list[idx] = element
        return new_list

    else:
        return new_list
if __name__  == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)
    print(new_list)
    print(my_list)
