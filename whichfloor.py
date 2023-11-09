maximum_stories = 40

userNum = int(input("\nOn what floor is your office? \n: "))
while (userNum > maximum_stories):
    print("you entered floor " + str(userNum) + ".\n But there are only " + str(maximum_stories) + " floors\n")
    userNum = int(input("On what floor is your office\n: "))

print("Congrats! You work on floor : " + str(userNum) + "\n\n")