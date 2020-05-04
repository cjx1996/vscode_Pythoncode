import time #import time module to test the O of function
def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
       if arr[i]<smallest:
           smallest=arr[i]
           smallest_index=i
    return smallest_index
def selectionSort(arr):
    newArr=[]
    j=len(arr)
    if j==0: 
        j=1 
    for i in range(j):
        i=i
        smallest=findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
print (selectionSort([5,3,5,67,875,12]))
print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))