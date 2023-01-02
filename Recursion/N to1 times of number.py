def main(i,n):
    if (i<1):
        return
    print(i)
    main(i-1,n)

if __name__ == "__main__":
    number = int(input("enter the number: "))
    main(number,number)