def insertion_sort(a):
    for i in range(1,len(a)):
        j=i-1
        key=a[i]

        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    print(a)

insertion_sort([1,4,3,2,11,7])