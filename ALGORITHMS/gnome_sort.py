def gnome(a):
    curr=1
    prev=0

    while True:
        if curr==len(a):
            print(a)
            return False

        if(a[curr]<a[prev]):
            a[curr],a[prev]=a[prev],a[curr]
            if(curr != 1):
                curr=prev
                prev-=1
        if(a[curr]>a[prev]):
            curr+=1
            prev+=1



gnome([4,2,1,7,0,6])