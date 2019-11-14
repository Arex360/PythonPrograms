Arr = []
ArrRange = int(input("Enter the range"))
for i in range(ArrRange):
    num = int(input("Enter number{} ".format(i+1)))
    Arr.append(num)
for number in Arr:
    for i in range(2,number):
        if(number % i == 0):
            print("{} is not prime".format(number))
            break
    else:
        print("{} is prime".format(number))
        
