def binarySearch(arr, key, l, r):
    if(l<=r):
        m = (l+r)//2
        if(arr[m]==key):
            return m
        elif(arr[m]<key):
            return binarySearch(arr, key, m+1, r)
        elif(arr[m]>key):
            return binarySearch(arr, key, l, m-1)
    else:
        return -1

arr = [50,20,60,40,30,70,80,10]
arr.sort()
key = 80
ans = binarySearch(arr, key, 0, len(arr)-1)
print("Sorted Array :", arr)
print("Position :", ans+1)