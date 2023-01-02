def fibonacci(n):
    if (n <= 1): 
        return n
    last = fibonacci(n-1)
    secondlast = fibonacci(n-2)
    return last + secondlast
    
if __name__=="__main__":
    number = int(input("Enter the number: "))
    print(fibonacci(number))