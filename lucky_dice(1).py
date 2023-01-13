import random

import time
from time import sleep
welcome="""
::|    ::| ::| ,::::\::| ::|::| ::|  ::::::\::::::| ,::::\::::::|
::|    ::|_::|::|    :::::<  ::::/   ::| ::|  ::|  ::|    :::>   
::::::|`:::::| '::::/::| ::|  ::|    ::::::/::::::| '::::/::::::|"""

print("GAME LOADING!! PLEASE WAIT....")
sleep(2)
animation = ["■□□□□□□□□□ 10%","■■□□□□□□□□ 20%", "■■■□□□□□□□ 30%", "■■■■□□□□□□ 40%", "■■■■■□□□□□ 50%", "■■■■■■□□□□ 60%", "■■■■■■■□□□ 70%", "■■■■■■■■□□ 80%", "■■■■■■■■■□ 90%", "■■■■■■■■■■ 100%"]

for i in range(len(animation)):
    sleep(1)
    print(animation[i % len(animation)])
print("\n")

print(welcome)

user=input("What is your name? ")
print("Hello", user)
play= input("Are ready for a dare adventure? yes/no ")
if play.lower()== "yes" or "y":
  print("~~~~~~~ GAME BEGINS ~~~~~~~")
else:
  print("Exit")
print("There are 4 Categories of winning in this game ")
Gameboard="""
=========|==================================================||
Any      ||   Hi    ||   9   ||   10  ||    11   ||   12    ||
Double   ||         ||       ||       ||         ||         ||       
         ||   3.4   ||  8.5  ||  11.5 ||   17.0  ||   34.0  ||    
 5.7     |==================================================||  
         ||   Mid       ||   8       ||   7      ||    6    ||        
         ||             ||           ||          ||         ||  
         ||   2.2       ||  6.9      ||  5.5     ||   6.9   ||          
=========|==================================================||      
mix      || Lo      ||   2   ||   3   ||    4    ||    5    ||
         ||         ||       ||       ||         ||         ||
         || 3.4     ||  34.0 ||  17.0 ||  11.5   ||   8.5   ||             
1.14     ||=================================================||   
         ||     Even              ||          Odd           ||  
         ||                       ||                        ||   
         ||      1.94             ||           1.94         ||  
=========||=================================================||
"""  
level="""Hint:
    => Category 1 : Double or Mix 
    => Category 2 : Even or Odd
    => Category 3 : Hi, Mid and Lo
    => Category 4 : Numbers between 2 and 12
    """
print(Gameboard)
print(level)
play_again = 'y'
while play_again == 'y':
    hi = [9,10,11,12]
    mid = [8,7,6]
    low= [2,3,4,5]
    DICE_ART = {
    
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }
    
    
    DIE_HEIGHT = len(DICE_ART[1])
    DIE_WIDTH = len(DICE_ART[1][0])
    DIE_FACE_SEPARATOR = " "
    
    res = False
    
    def roll_dice():
        dice1=[1,2,3,4,5,6]
        dice2=[1,2,3,4,5,6]
        dice_row= []
        random_num1= random.choice(dice1)
        random_num2= random.choice(dice2)
        total= random_num1 + random_num2
        dice_row.append(random_num1)
        dice_row.append(random_num2)
        return dice_row
    
    def generate_dice_faces_diagram(dice_values):
        dice_faces = []
        for value in dice_values:
            dice_faces.append(DICE_ART[value])
        # Generate a list containing the dice faces rows
        dice_faces_rows = []
        for row_idx in range(DIE_HEIGHT):
            row_components = []
            for die in dice_faces:
                row_components.append(die[row_idx])
            row_string = DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string)
        # Generate header with the word "RESULTS" centered
        width = len(dice_faces_rows[0])
        diagram_header = " RESULTS ".center(width, "~")
        dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
        return dice_faces_diagram
    
    
    point_board =   {  "hi": 3.40,  9: 8.50,  10: 11.50,  11: 17.00,  12: 34.00,  "mid": 2.20,  8: 6.90,  7: 5.50,  6: 6.90,  "low": 3.40,  2: 34.00,  3: 17.00,  4: 11.50,  5: 8.50,  "double": 5.70,  "mix": 1.14, "odd": 1.94, "even": 1.94}
        
      
    def chkList(lst):
        if len(lst) < 0 :
            res = True
        res = lst.count(lst[0]) == len(lst)
        if(res):
            return "double"
        else:
                return "mix"
            
    def chkEvenOdd(value):
         if (value % 2) == 0:
            return "even"
         else:
            return "odd"
            
    def add(lst):
        return sum(lst)
    
    def animate():
        sys.stdout.write('\r dice rolling |')
        time.sleep(0.1)
        sys.stdout.write('\r dice rolling /')
        time.sleep(0.4)
        sys.stdout.write('\r dice rolling -')
        time.sleep(0.4)
        sys.stdout.write('\r dice rolling \\')
        time.sleep(0.4)
        sys.stdout.write('\r dice rolling |')
        time.sleep(0.4)
        sys.stdout.write('\r dice rolling /')
        time.sleep(0.4)
        sys.stdout.write('\r dice rolling -')
        time.sleep(0.4)
        sys.stdout.write('\r dice rolling \\')
        time.sleep(0.4)
        
    def range_score(total):
        if (total in hi):
            return "hi"
        elif(total in mid):
            return "mid"
        elif(total in low):
            return "low"
    
    def parse_input(input_string):
        if input_string.strip() in {"1", "2", "3", "4"}:
            return int(input_string)
        else:
            print("Please enter a number from 1 to 4.")
            
    
  
    # 1. Get and validate user's input
    category_input = input("Select a category between ? [1-4] ")
    category = parse_input(category_input)
    roll_dice= roll_dice()
    if(category==1):
        category_one = input("Enter (double or mix) as input to predict dice pair?  ")
        print("You entered "+ category_one.lower() +"")
        print("Please wait!! Dice rolling....")
        animate() 
        dice_face_diagram = generate_dice_faces_diagram(roll_dice)
        print(f"\n{dice_face_diagram}")
        result=chkList(roll_dice)
        print(result)
        score=point_board[result]
        
        if(category_one.lower()==result):
            print("Bravo!!! your prediction is correct and your score: ",score)
        else:
            print("Sorry your prediction is wrong!!, your want to play again?")
    
    elif(category==2):
        category_two = input("Enter (even or odd) as input to predict dice pair?  ")
        print("You entered "+ category_two +"")
        print("Please wait!! Dice rolling....")
        animate()
        dice_face_diagram = generate_dice_faces_diagram(roll_dice)
        print(f"\n{dice_face_diagram}")
        total=add(roll_dice)
        result=chkEvenOdd(total)
        print(result)
        score=point_board[result]
        if(category_two.lower()==result):
            print("Bravo!!! your prediction is correct and your score: ",score)
        else:
            print("Sorry your prediction is wrong!!, your want to play again?")
            
    elif(category==3):
        category_three = input("Enter (hi or mid or lo) as input hint:hi={9,10,11,12},mid={8,7,6} and lo={2,3,4,5} to predict dice pair?  ")
        print("You entered "+ category_three +"")
        print("Please wait!! Dice rolling....")
        animate()
        dice_face_diagram = generate_dice_faces_diagram(roll_dice)
        print(f"\n{dice_face_diagram}")
        total=add(roll_dice)
        result=range_score(total)
        print(result)
        score=point_board[result]
        if(category_three.lower()==result):
            print("Bravo!!! your prediction is correct and your score: ",score)
        else:
            print("Sorry your prediction is wrong!!, your want to play again?")
           
    elif(category==4):
        category_four = input("Enter a number between range 1 to 12 as input to predict dice pair?  ")
        print("You entered "+ category_four +"")
        print("Please wait!! Dice rolling....")
        animate()
        dice_face_diagram = generate_dice_faces_diagram(roll_dice)
        print(f"\n{dice_face_diagram}")
        result=add(roll_dice)
        print(result)
        score=point_board[result]
        if(category_four==result):
            print("Bravo!!! your prediction is correct and your score: ",score)
        else:
            print("Sorry your prediction is wrong!!, your want to play again?")
    
    play_again = input("Want to play again(y/n): ")

print("~~~~~~~ GAME ENDS ~~~~~~~")
