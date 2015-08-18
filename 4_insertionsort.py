def insertionSort(mylist):
   count = 0
   for i in range(1,len(mylist)):
     count = count + 1
     current = mylist[i]
     pos = i

     while pos>0 and mylist[pos-1]>current:
         mylist[pos]=mylist[pos-1]
         pos = pos-1
         mylist[pos]=current
   print "count is",count
mylist = [54,26,93,17,77,31,44,55,20]
insertionSort(mylist)
print(mylist)