def duplicate(arr):
    tortoise=arr[0]
    hare=arr[0]

    while True:
        tortoise=arr[tortoise]
        hare=arr[arr[hare]]

        if(tortoise==hare):
            break

    ptr1=arr[0]
    ptr2=tortoise

    while ptr1!=ptr2:
        ptr1=arr[ptr1]
        ptr2=arr[ptr2]

    return ptr1

print(duplicate([1,2,3,4,5,6,1]))

