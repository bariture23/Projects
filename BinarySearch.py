#start of code
def BinarySearch(the_array, low, high, x):
    if high >= low:
        #if the high is more than the lowest number
        if the_array[(high+low)//2] == x:
            return (high+low)//2
        elif the_array[(high+low)//2] > x:
            return BinarySearch(the_array, low, (high+low)//2 - 1, x)
        else:
            return BinarySearch(the_array, (high+low)//2 + 1, high, x)
    else:
        return -1
#end of the loop

def main():
    ARRAY = [11, 21, 33, 40, 50]
    #the list of numbers in the array
    
    Finder = BinarySearch(ARRAY, 0, 4, 21)
    
    if Finder != -1:
#if loop when the index is found or not found
        print("The element found at index", Finder)
#the element is found in the index
    else:
     #else loop
        print("The element not found!")
#in case the element isn't found
if __name__ == "__main__":
    main()
#end of code