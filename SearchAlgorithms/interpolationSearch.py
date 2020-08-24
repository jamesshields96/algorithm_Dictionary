# This search algorithm works on the probing position of the required value
# For this algorithm to work properly, the data collection should be in a sorted form and
# equally distributed. Initially, the probe position is the position of the 
# middle most item of the collection. If a match occurs, the index of the item is returned.
# If the middle item is greater than the item, then the probe position is again calculated
# in the sub-array to the right of the middle item.
# Otherwise, the item is searched in the subarray to the left of the middle item.
# This process continues on the sub-array as well until the size of the subarray reduces to zero


def intPolSearch(values, x):
    idx0 = 0
    idxn = (len(values) - 1)

    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:


# Find the mid point

        mid = idx0 +\
               int(((float(idxn - idx0)/( values[idxn] - values[idx0]))
                    * ( x - values[idx0])))

# Compare the value at mid point with search value
        if values[mid] == x:
            return "Found " + str(x) + " at index " + str(mid)

        if values[mid] < x:
            idx0 = mid + 1
    return "Searched for element is not in the list"

list = [2,4,6,7,8,10,12]
print("The list contains the numbers:")
print(list)
print("Search for the number 7")
print(intPolSearch(list, 7))

