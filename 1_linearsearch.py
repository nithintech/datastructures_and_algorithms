def linearsearch(myitem, mylist):
    found = False
    count = 0
    while count < len(mylist) and not found:
        if mylist[count] == myitem:
            found = True
        count = count + 1
    return found, "search count is", count


search = True
numlist = [1, 6, 12, 25, 36, 42, 34, 47, 27, 67, 64, 36]
while search:
    item = int(raw_input("enter item ???\n"))
    isfound = linearsearch(item, numlist)
    if isfound[0]:
        print linearsearch(item, numlist)
    else:
        print "not found"
        if not isfound[0]:
            newitem = raw_input("Do you want to add this item???y/n.\n")
        if newitem == 'y':
            numlist.append(item)
            print item, "was added to your list."
            print numlist
        else:
            print item, "was not added to your list."