def name(start_number,end_number):
    if (start_number > end_number):
        return
    print("vinay")
    main(start_number+1 , end_number)
 
if __name__=="__main__":
    start_number = 1
    end_number = int(input("enter the number"))
    name(start_number,end_number)