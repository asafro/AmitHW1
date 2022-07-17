#!/usr/bin/python3


"""
A function that checks if a string is a valid Yes or No answer
"""
def isLegalYesNoAnswer(answerString):
  legalAnswers = ["Y", "N"]
  return answerString in legalAnswers

# Tell the user hello
print("Hello adventurer!")
print("In order to enter the king's court one must identify himeself")

# Ask the user for their name
username = input("Please enter a username: ")
print(f"Hello {username} you are allowed to enter!")

# Ask the user if they want to meet the king
wantToSeeKingString = ""

while not isLegalYesNoAnswer(wantToSeeKingString):
  wantToSeeKingString = input("The King is interested in meeting with you.\nDo you confirm? (Y/N)")

# Quit if user does not want to meet the king
if not wantToSeeKingString == "Y":
  print(f"bye bye {username} and thank you for playing")
  exit()


#TODO: we have the username and they want to meet the king, code the rest of the adventure...
print("Yeah baby, let's get this party started")

