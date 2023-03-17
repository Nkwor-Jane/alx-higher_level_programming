def search_replace(my_list, search, replace):
    new = my_list[:]
    new = [x if x != search else replace for x in my_list]
    return (new)
