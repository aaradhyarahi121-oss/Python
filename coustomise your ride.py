print("Select your ride:")
print("1.Bike")
print("2.Car")

choice = int(input("Enter your choice:"))

if( choice == 1):
    print("what type of bike?")
    print("1.Scooty\n")
    print("2.Scooter\n")

    choice2=int(input("Enter your choice2:"))
    if choice2==1:
        print("You have selacted scooty")
    else:
        print("You have selacted scooter")    

        
elif( choice == 2):
    print("what type of car?")
    print("1.Sedan\n")
    print("2.XUV\n")

    choice3=int(input("Enter your choice3:"))
    if choice3==1:
        print("You have selacted sedan")
    else:
        print("You have selacted XUV")
else:
    print("wrong choice!")        