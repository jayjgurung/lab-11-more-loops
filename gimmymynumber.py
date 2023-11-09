num = int(input("Gimme a number greater than 100!... "))
while(num<=100):
    print(str(num) + " is not greater than 100!")
    num = int(input("Not what I asked for.. Gimme a number greater than 100!...\n\n"))
print(str(num) + " is greater than 100! Congrats..\n")