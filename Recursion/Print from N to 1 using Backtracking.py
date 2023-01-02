def main(i,n):
    if (i>n):
        return
    main(i+1,n)
    print(i)

if __name__=="__main__":
    number = int(input("enter the number: "))
    main(1, number) 