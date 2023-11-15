def countDown(start):
    print(start)
    if start == 1:
        print ("Happy New Year!")
        return;
    nextNumber = start - 1 
    countDown(nextNumber)

userInput = int(input("Enter a countdown number : "))

countDown(userInput)