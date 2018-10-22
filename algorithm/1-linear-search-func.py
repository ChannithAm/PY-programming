def linear_search(item_list, item):
    found = False

    for key, value in enumerate(item_list):
        print('Position: %d, Value: %d, Search item: %d' %(key, value, item))
        if value == item:
            found = True
            print('Element found in the list at location %d' %(key))
            break
    if not found:
        print('Element not found')

item_list = [1, 2, 3, 4, 23, 55, 23, 44, 55, 199, 55, 111]
item = 55
linear_search(item_list, item)
