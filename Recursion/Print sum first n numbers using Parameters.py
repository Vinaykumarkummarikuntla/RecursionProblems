def sum_first_n_numbers(number,sum):
    if (number<1):
        print(sum)
        return
    sum_first_n_numbers(number-1,sum+number)

if __name__=="__main__":
    number = int(input("enter the number: "))
    sum_first_n_numbers(number,0 )