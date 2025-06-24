number = int(input(" Please Enter any Positive Integer : "))
if(number % 5 == 0) and (number % 11 == 0) :
    print("Given Number {0} is Divisible by 5 and 11 ".format(number))
elif (number % 5!= 0) and  (number % 11!= 0):
    print("Given Number {0} is not Divisible by 5 and 11".format(number))
elif (number % 5 == 0):
    print("Given Number {0} is Divisible by 5".format(number))
elif (number % 11 == 0):
    print("Given Number {0} is Divisible by 11".format(number))
else:
    print("Given Number {0}  Divisible by 5 and 11".format(number))gitgit