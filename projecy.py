print("Welcome to my Bible quiz")

playing = input("Do you want to play? yes/no ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play 😎")
score = 0

question = input("In what city was Jesus born? ")
if question.lower() == "bethlehem":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("Who was the father of Jesus? ")
if question.lower() == "joseph":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("Who was the mother of Jesus? ")
if question.lower() == "mary":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("How many books are in the bible? ")
if question.lower() == "66":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + " %")
print("Thank you for playing😎")
