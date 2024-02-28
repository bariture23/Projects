array = [31,28,33,42,51,63,71]
def sorting(array,low,high):
    i = low-1
    pivot = array[high]
    for j in range(low,high):
        if array[j] <= pivot:
            i+=1
            array[i],array[j] = array[j],array[i]
        else:
            j+=1
    i+=1
    array[i],array[high] = array[high],array[i]
    return i
def quick_sort(A,low,high):
    if low<high:
        left_off = sorting(A,low,high)
        quick_sort(A,low,left_off-1)
        quick_sort(A,left_off+1,high)
    return A
print(quick_sort(array,0,len(array)-1))