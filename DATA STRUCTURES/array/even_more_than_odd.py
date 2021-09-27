def rearrange(arr):

    for i in range(1,len(arr)):
        if i%2==0:
            if(arr[i]<arr[i-1]):
                arr[i],arr[i-1]=arr[i-1],arr[i]
        else:
            if(arr[i]>arr[i-1]):
                arr[i-1],arr[i]=arr[i],arr[i-1]
    return arr
print(rearrange([1,2,6,2,19,4]))