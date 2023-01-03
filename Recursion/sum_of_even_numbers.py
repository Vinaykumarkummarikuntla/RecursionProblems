def main(n):
    if (n == 0):
        return 0
    return n + main(n-2)

if __name__=="__main__":
    number = int(input("enter the number: "))
    print(main(number))
