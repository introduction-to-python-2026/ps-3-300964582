def move(my_list, direction):
    index_of_one = my_list.index(1)

    # if we want to move right
    if direction == "right":
        # check if the pig is in the right edge- don't change location
        if index_of_one == len(my_list) - 1:
            return my_list
        # else move right
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

# if we want to move left
    elif direction == "left":
        # check if the pig is in the left edge- don't change location
        if index_of_one == 0:
            return my_list
        #  else move left
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
