# weight calculator
# print("Welcome to BMI calculator")

# def get_bmi() :
#     Height = float(input("please input your height : "))
#     Weight = float(input("please input your weight (in kg) : "))

#     bmi = Weight / (Height ** 2)
#     return bmi

# bmi_result = get_bmi()

# print(f"Your bmi is around", int(bmi_result))

# weight calculator modifying with description
# print("Welcome to BMI calculator")

# def get_bmi() :
#     Height = float(input("please input your height : "))
#     Weight = float(input("please input your weight (in kg) : "))

#     bmi = Weight / (Height ** 2)
#     return bmi

# bmi_result = get_bmi()

# def print_bmi_category(bmi_result):
#     if bmi_result < 18.5 :
#         return("you are underweight")
#     elif 18.5 <= bmi_result <=24.9 :
#         return("your weight is normal")
#     elif 25 <= bmi_result <= 29.9 :
#         return("your weight is overweight")
#     elif 30 <= bmi_result <= 34.9 :
#         return("your weight is obesity types I")
#     elif 35 <= bmi_result <= 39.9 :
#         return("your weight is obesity types II")
#     else :
#         return("you are extremely obesity")
    
# bmi_category = print_bmi_category(bmi_result)
# print(f"your bmi is around {int(bmi_result)}, {bmi_category}")

# def main():
#   age = getAge()
#   weight = getWeight()
#   birthMonth = getBirth()
#   correct(age,weight,birthMonth)

# def getAge():
#   age = float(input("Guess the age.\t"))
#   return age
# def getWeight():
#   weight = float(input("Guess the weight.\t"))
#   return weight
# def getBirth():
#   birthMonth = input("Guess the month.\t")
#   return birthMonth
# def correct(age,weight,birthMonth):
#   if age <= 25:
#      print ("Congratulations, the age is 25 or less")
#   else:
#     print ("You did not correctly guess the age")
#   if weight <= 128:
#     print ("Congratulations, the weight is 128 or more")
#   else:
#     print ("You did not correctly guess the weight")
#   if birthMonth == "April":
#     print ("Congratulations, the month is April")
#   else:
#     print ("You did not correctly guess the month")

# main()

#rock paper, scisor and rock game 
# 1. import random to convert random decision or choice from the computer
import random

# 2. print the welcome information alongside creation for score band which categorized into 3 side : user, com, draw
def main() :
    print("Let's play rock-paper-scissor! ")
    score = {"user" : 0, "computer" : 0, "ties" : 0}

# 3. create logic command for user , computer where once both user and computer made their decisions, the program will pick who's winner from the game. While True (loop function) always ended with break command. 
    while True :
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. The computer chose {computer_choice}.")
        winner = determine_winner(user_choice, computer_choice)
        print(winner)
        if winner == "you win!" :
            score["user"] += 1
        elif winner == "computer win!" :
            score["computer"] += 1
        else :
            score["ties"] += 1
        print(f"score : user - {score['user']}, computer - {score['computer']}, ties - {score['ties']}")
        if not play_again():
            break

# 4. we create the computer behavior by use random.choice(options) so the computer able to run action to compete with user. .lower() is used to convert the user's choice to lowercase before checking.
def get_computer_choice():
    options = ["rock", "paper", "scissor"]
    return random.choice(options)

def get_user_choice():
    while True : 
        user_choice = input("Choose rock, paper or scissor : ")
        if user_choice.lower() in ["rock", "paper", "scissor"] : 
            return user_choice.lower()
        else :
            print("invalid choice. please try again!")

# 5. determine the rule of game rock beat scissor, paper beat rock and scissor beat paper
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice : 
        return("it's a tie!")
    elif user_choice == "rock" and computer_choice == "scissor" :
        return("you win!")
    elif user_choice == "paper" and computer_choice == "rock" :
        return("you win!")
    elif user_choice == "scissor" and computer_choice == "paper" :
        return("you win!")
    else :
        return("computer win!")

# 6. the last option is we create the option for user if they want to play again or not. 
def play_again():
    while True :
        choice = input("Do you want to play again ? (y/n): ")
        if choice.lower() == "y" :
            return True
        elif choice.lower() == "n":
            return False
        else : 
            print("invalid choice. please try again")
    
# 7. main() is a function that is commonly used in programming to represent the starting point of a program. It usually contains the primary logic and control flow of the program. In Python, you can define your own main() function to execute when your program starts. This is often seen in scripts and small programs.            
main()