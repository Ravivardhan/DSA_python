
#find min in array and check if it divides all the other elements in the array

import sys

def check(arr):
    min=sys.maxsize

    for i in arr:
        if i<min:
            min=i

    for i in arr:
        if not i%min==0:
            return False

    print("smallest value in the array",min)

    return True
arr=[100,200,300,600]
#print(check(arr))


#find an element in the array such that it divides all the other elements

def div(arr):
    index=0
    for i in arr:
        if not i%arr[index]==0:
            return False
    print(arr[index])
    return True


arr2=[10,200,300,400]
print(div(arr2))