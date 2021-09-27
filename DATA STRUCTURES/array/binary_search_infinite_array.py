def binary_search(arr,start,end,val):
    while start <= end:
        mid=(start+end)//2
        if( arr[mid] == val):
            return mid
        elif val>arr[mid]:
            start+=1
        else:
            end -=1
    return -1

def search(arr,val):

    start=0
    end=1
    temp=arr[0]

    while temp<val:
        start=0
        end+=1
        temp=arr[end]
    ans=binary_search(arr,start,end,val)
    if ans==-1:
        return "value not found"
    else:
        return "value found at index {}".format(ans)

arr=[1,2,3,4,5,6,7]
print(search(arr,7))