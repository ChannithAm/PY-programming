
array = [2,6,1,7,4,5,9,6,43,2,2,9,0,21]
array.sort()

def printLine(count):
    for i in range(count):
        print("=", end="")
    print()

def search(alist, value):
    first = 0
    last = len(alist) - 1
    found = False
    comparisons = 0
    index = -1

    while first <= last and not found:
        print("Compare {}".format(comparisons + 1))
        print("First: {}, alist({}) = {}".format(
            first, first, alist[first]
        ))
        print("Last: {}, alist({}) = {}".format(
            last, last, alist[last]
        ))
        comparisons +=1
        midpoint = (first + last)//2
        if value == alist[midpoint]:
            found = True
            index = midpoint
        else:
            if value < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    print("Number of comparisons is: {}".format(comparisons))
    return index

printLine(50)
print(array)

printLine(50)
location = search(array, 43)
if location != -1:
    print("43 is at {}".format(location + 1))
else:
    print("43 is not found")
