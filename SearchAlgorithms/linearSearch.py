# In linear search, a sequential search is made over all items one by one
# Every item is checked and if a match is found then that particular item is returned
# Otherwise the search continues till the end

def linear_search(values, search_for):
    search_at = 0
    search_res = False

# Math the value with each data element
    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1

    return search_res

list = [64, 22, 33, 44, 55, 99, 86, 70]
print("List of numbers:")
print(list)
print("Does the list contain 33? ")
print(linear_search(list, 33))
print("Does the list contain 104? ")
print(linear_search(list, 104))

