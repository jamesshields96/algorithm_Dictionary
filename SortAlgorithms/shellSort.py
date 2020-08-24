# Shell Sort involves sorting elements which are away from each other
# We got a large sublist of a given list and go on reducing the size of the list until all elements are sorted
# The below program finds the gap by equating it to half of the length of the list size
# and then starts sorting all the elements in it
# We then keep resetting the gap until the entire list is sorted

def shellSort(input_list):
    
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i

# Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

# Reduce the gap for the next element

        gap = gap // 2


list = [22,55,11,33,105,63,25,9,900]
print("Before the Shell sort")
print(list)
print("After the Shell Sort")
shellSort(list)
print(list)