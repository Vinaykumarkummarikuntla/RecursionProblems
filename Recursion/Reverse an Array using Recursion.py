def reverse_array(i,array,n):
    if (i >= n/2):
        return 
    # swap
    array[i],array[n-i-1] = array[n-i-1], array[i]
    reverse_array(i+1,array,n)
    
if __name__=="__main__":
    array = []
   # number of elements as input
    n = int(input("Enter number of elements : "))
    # iterating till the range
    for i in range(0, n):
        ele = int(input())
        array.append(ele) # adding the element
    print(array)
    reverse_array(0,array,n)
    # result
    for i in range(0,n):
        print(array[i])