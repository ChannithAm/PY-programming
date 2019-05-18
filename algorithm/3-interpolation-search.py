def interpolation_search(alist, x):
    n = len(alist)
    low = 0
    high = n - 1

    while((alist[high] != alist[low]) and (x >= alist[low]) and (x <= alist[high])):
        mid = low + ((x - alist[low]) * (high - low) // (alist[high] - alist[low]))
        print("low = {}, high = {}, mid = {}".format(low, high, mid))
        if(alist[mid] < x):
            low = mid + 1
        elif(x < alist[mid]):
            high = mid - 1
        else:
            return mid
    
    if(x == alist[low]):
        return low
    else:
        return -1


alist = [1,2,44,53,55,67,78,89,90,100,101,111,142,145,156]
while True:
    for i in range(len(alist)):
        print("{}, ".format(alist[i]), end="")
    
    x = int(input("\nEnter x = "))
    if(x == 0):
        break
    print("Search result: {}".format(interpolation_search(alist, x)))