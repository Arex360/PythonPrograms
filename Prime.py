Arr = []
ArrRange = int(input("Enter the range: "))
for i in range(ArrRange):
  temp = int(input("Enter the integer{}".format(i+1)))
  Arr.append(temp)
for number in Arr:
  for j in range(2,number):
    if(number % i == 0):
      print("{} is not a prime number".format(number))
      break
  if number == 1:
    print("1 is not a prime number")
  else:
    print("{} is a prime number".format(number))
             

