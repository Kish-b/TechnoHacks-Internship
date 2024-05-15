# ASCII ART of  Rock , Paper and Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Importing random Module

import random


hand =[rock,paper,scissors]   # list to store ASCII art of rock,paper and scissors

print("\n\n\t\t\t !!! Welcome to Rock Paper Scissor Game !!!\n")

while True:

    # My Decision 
    My_choice= int(input("What would you choose ?\nTYPE '0' for Rock , '1' for Paper and '2' for Scissor \n"))

    # checkingfor invalid values like "Above 2 -> 4 , 543 , 67 , etc..."  or "Negative Values ->  -2 , -342 , etc...."

    if My_choice>2 or My_choice<0 :
        print("\n! Invalid input ! , Enter the correct input\n")

    # Actual Code part
    else :  
        print("\nYou choose :  \n",hand[My_choice])

        #computer random Decision
        Computer_choice = random.randint(0,2)
        print("\nComputer choose :  \n",hand[Computer_choice])

        #  Decision Part - Win , Lose or Draw

        if My_choice==2 and Computer_choice==0 :
            print("\n !! YOU LOSE !!\n")

        elif My_choice==0 and Computer_choice==2 :
            print("\n !! YOU Won !!\n")

        elif  My_choice < Computer_choice:
            print("\n !! YOU LOSE !!\n")

        elif My_choice > Computer_choice  :
            print("\n !! YOU Won !!\n")

        else :
            print("\n !! DRAW !!\n")
    
    replay = int (input("\nEnter 0 to PLAY or 1 to EXIT : "))
    if replay == 0 :
        pass
    elif replay == 1:
        break
    else:
        print("\n! Invalid input ! , Enter the correct input\n")

