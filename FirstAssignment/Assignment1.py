#Task one 
Comb = "+--+--+--+ \n|  |  |  |"
Line = "+--+--+--+"
i = 1

while i < 4:
    print(Comb)
    i=i+1

print(Line)

#Task two a vending machine task that returns change value.

#Define constants.
PENNIES_PER_DOLLAR =100
PENNIES_PER_QUATER=25

#Obtain input from user 
UserInput=input("Enter bill value eg 1 = $1 bill: ")
BillValue = int(UserInput)
Userinput=("Enter itemprice in pennies")
Itemprice=int(Userinput)

