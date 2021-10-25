def find_sum(arr,s):
    start=0
    i=1
    current_sum=arr[0]
    n=len(arr)-1
    while i<=n:

        if current_sum==s:
            return "sum found between {} and {}".format(start,i-1)

        current_sum=current_sum+arr[i]
        i+=1

        while current_sum>s and start<i:
            current_sum=current_sum-arr[start]
            start+=1
    return "sum not found"

arr=[15,2,4,8,9,5,10,23]
print(find_sum(arr,14))