#practicing if using userinput and managing time

#user data
Userdata = input("Enter your username.: ")
Userdata2= int(input("Enter your age.: "))
print("\bWelcome, \nI heard you want to know time gaps.",Userdata)

#time data
print("please use 24hr format eg.1300.")
Firsttime =input("Enter the first time you want to: \t ")
Hours =int(Firsttime[0:2])
Mins = int(Firsttime[2:])
Secondtime =input("Enter the second time you want to: \t ")
Hourstwo =int(Secondtime[0:2])
Minstwo= int(Secondtime[2:])

#Math calculations and if statements
if Secondtime > Firsttime:
    Firsttime = Hours * 60 + Mins
    Secondtime = Hourstwo * 60 + Minstwo
    
elif Secondtime < Firsttime:
    Firsttime = Hours * 60 + Mins
    Secondtime = (Hourstwo * 60 + Minstwo) + 1440
else:
    print("Same time entered.")
    exit()

#calculating the timediff
timediff= Secondtime - Firsttime
hoursalone = timediff // 60
minsalone = timediff % 60

print("The time gap is: ",hoursalone,"hours ",minsalone,"mins")

