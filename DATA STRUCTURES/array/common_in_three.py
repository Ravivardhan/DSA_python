def find_common(arr1,arr2,arr3):
    i=0
    j=0
    k=0

    while i<len(arr1) and j<len(arr2) and k<len(arr3):
        if(arr1[i]==arr2[j]==arr3[k]):
            return arr1[i]
        elif arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr3[k]:
            j+=1
        else:
            k+=1
arr1=[1,2,4,5,10]
arr2=[1,7,8,9,10]
arr3=[1,5,7,10,19]
print(find_common(arr1,arr2,arr3))