def counting_sort(a):
    max=0
    for i in a:
        if max<i:
            max=i
    c=[0]*(max+1)
    for i in range(0,max+1):
        for j in a:
            if i==j:
                c[i]+=1
    #print(c)
    for i in range(1,max+1):
        c[i]+=c[i-1]
    #print(c)
    sorted_array=[0]*len(a)
    for i in a:
        sorted_array[c[i]-1]=i
    print(sorted_array)
counting_sort([1,6,4,2,11,3,9,5])