def bubblesort(mylist):
	swaps = True
	while swaps:
	    swaps = False
	    count =0
	    for element in range(len(mylist)-1):
	    	count=count+1
	        if mylist[element] > mylist[element+1]:
	            swaps = True
	            temp = mylist[element]
	            mylist[element]=mylist[element+1]
	            mylist[element+1] = temp
        return "sortedlist is",mylist,"count is",count

mylist = [12,32,45,87,14,62]
sortedlist=bubblesort(mylist)
print sortedlist