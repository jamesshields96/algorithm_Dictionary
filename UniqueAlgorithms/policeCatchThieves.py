# O(n) time complexity
# finds the max number of thieves that the police can catch


def policeThief(arr, n, k):
    i = 0
    l = 0
    r = 0
    res = 0
    thi = []
    pol = []

    # store indices in list
    while i < n:
        if arr[i] == 'P':
            pol.append(i)
        elif arr[i] == 'T':
            thi.append(i)
        i += 1

        # Track the lowest current indicies of thief and police(thi and pol)
    while l < len(thi) and r < len(pol):

            # can still be caught
        if (abs(thi[l] - pol[r]) <= k):
            res += 1
            l += 1
            r += 1

        elif thi[i] < pol[r]:
            l += 1
        else:
            r += 1

    return res


# Driver program
if __name__ == '__main__':
    arr1 = ['P', 'T', 'T', 'P', 'T']
    k = 2
    n = len(arr1)
    print(("Maximum thieves caught: {}".
         format(policeThief(arr1, n, k))))

    arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
    k = 2
    n = len(arr2)
    print(("Maximum thieves caught: {}".
          format(policeThief(arr2, n, k))))

    arr3 = ['P', 'T', 'P', 'T', 'T', 'P']
    k = 3
    n = len(arr3)
    print(("Maximum thieves caught: {}".
          format(policeThief(arr3, n, k))))
