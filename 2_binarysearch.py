def binarysearch(myitem, mylist):
    found = False
    bottom = 0
    top = len(mylist) - 1
    count = 0
    while bottom <= top and not found:
        middle = (bottom+top)//2
        if mylist[middle] == myitem:
            found = True
        elif mylist[middle] < myitem:
            bottom = middle + 1
        else:
            top = middle - 1
        count = count + 1
    return found,"no of searches",count


search = True
numlist = [1, 6, 12, 25, 36, 42, 34, 47, 27, 67, 64, 36]
while search:
    item = int(raw_input("enter item ???\n"))
    isfound = binarysearch(item, numlist)
    if isfound[0]:
        print binarysearch(item, numlist)
    else:
        print "not found"
        if not isfound[0]:
            newitem = raw_input("Do you want to add this item???y/n.\n")
        if newitem == 'y':
            numlist.append(item)
            print item, "was added to your list."
            print numlist
        