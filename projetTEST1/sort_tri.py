def trier(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list
