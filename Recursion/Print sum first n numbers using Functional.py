def sum_first_n_numbers(number):
    if (number == 0):
        return 0
    return number + sum_first_n_numbers(number-1)

if __name__=="__main__":
    number = int( input("enter the number: "))
    print(sum_first_n_numbers(number))