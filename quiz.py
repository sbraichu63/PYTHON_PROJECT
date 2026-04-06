print("Weclome to my quiz")

playing = input('Do you want to play the quiz? ').lower()

if playing != "yes":
    quit()
marks = 0

answer = input("what is the full form of cpu? ")
if answer == "central processing unit":
    print("correct")
    marks += 1
else:
    print("incorrect")

answer = input("what is the full form of GPU? ")
if answer == "graphical processing unit":
    print("correct")
    marks += 1
else:
    print("incorrect")

answer = input("what is the full form of POST? ")
if answer == "power on self test":
    print("correct")
    marks += 1
else:
    print("incorrect")

answer = input("what is the full form of ROM? ")
if answer == "read only memory":
    print("correct")
    marks += 1
else:
    print("incorrect")

answer = input("what is the full form of UPS? ")
if answer == "uninteruptable power supply":
    print("correct")
    marks += 1
else:
    print("incorrect")

print("The number of quizes you got right is:",marks)