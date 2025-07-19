print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Choose your direction.")
direction = input('  Take "left" or "right".\n').lower()

if direction == "left":
    choice = input('You\'ve come to a lake.'
                   'There is an island in the middle of the lake.\n'
                   '  Type "wait" to wait for a boat or '
                   'type "swim" to swim across:\n').lower()
    if choice == "wait":
        color = input('You arrived at the island unharmed.'
                     'There is a house with with 3 doors.\n'
                     '  One "red", one "blue", and one "yellow".'
                     'Which color do you choose?\n').lower()
        if color == "yellow":
            print("Congratulations, you've found the treasure."
                  "You've Won!!!")
        elif color == "blue":
            print("Oops, you've entered a room with a beast."
                  "Game Over.")
        elif color == "red":
            print("Oops, you've entered a room on fire."
                  "Game Over.")
        else:
            print("Game Over.")
    else:
        print("You've been attacked by an angry trout. Game Over.")
else:
    print("Oops, you fell into a hole. Game Over.")


