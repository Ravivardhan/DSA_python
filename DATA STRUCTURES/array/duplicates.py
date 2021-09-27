def duplicate(arr):
    res=[]
    for x in arr:
        if arr[abs(x)-1]<0:
            res.append(abs(x))

        else:
            arr[abs((x)-1)]*=-1
    return res
arr=[1,2,2,4,5,5,6]
print(duplicate(arr))