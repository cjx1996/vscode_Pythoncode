histroy1=('RADIOHEAD',156)
history2=('KISHORE',141)
history3=('THE BLAACK KEYS',35)
history4=('NEUTRAL MILK HOTEL',94)
history5=('BECK',88)
history6=('THE STOKES',61)
history0=('WILCO',111)
bands=[history0,histroy1,history2,history3,history4,history5,history6]
#print(bands)
test=bands[0][1]
print(test)
def findbiggest(arr):
    biggest=arr[0][1]
    biggest_index=0
    for i in range(1,len(arr)):
       if arr[i][1]>=biggest:
           biggest=arr[i][1]
           biggest_index=i
    return biggest_index
def  selection_Sort(arr):
    newArr=[]
    for i in range(len(arr)):
        i=i
        biggest=findbiggest(arr)
        newArr.append(arr.pop(biggest))
    return newArr
print(selection_Sort(bands))
  
