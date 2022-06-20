def partition(a, low, high):
    pivot = a[low]
    i = low
    j = high

    while i < j:
        while a[i]<= pivot:
            i += 1
        while a[j] > pivot:
            j-= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[low], a[j] = a[j], a[low]
    return j

def quicksort(a, l, h):
    if l < h:
        j = partition(arr,l, h)
        quicksort(arr,l,j)
        quicksort(arr, j+1, h)

arr = [10,6,7,1,3,4,11]
quicksort(arr, 0, 6)
print(arr)