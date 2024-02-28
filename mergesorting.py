array = [11,12,13,14,15,10,16,17,18,19]
def mergesorting(array):
    if len(array) == 1 < 2: return array
    else:
        mid = (len(array))//2
        left = mergesorting(array[:mid])
        right = mergesorting(array[mid:])
        order = merge(left,right)
        return order
def merge(left,right):
    rarray = []
    j=0
    i=0
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            rarray.append(left[i])
            i+=1
        else:
            rarray.append(right[j])
            j+=1
    rarray += right[j:]
    rarray += left[i:]
    return rarray
mergesorting(array)
print(mergesorting(array))