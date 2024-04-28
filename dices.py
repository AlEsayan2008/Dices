#Dice game
import random


def algoritm_of_game(your_first_dice, your_second_dice, his_first_dice, his_second_dice): 
        while True:
            if your_command.lower() == "to threw":    
                if your_first_dice + your_second_dice == his_first_dice + his_second_dice:
                    print("It is tie.")
                    print(f"Sum of your dices: {your_first_dice + your_second_dice} is equal to the sum of his dices: {his_first_dice + his_second_dice}")
                if your_first_dice + your_second_dice > his_first_dice + his_second_dice:
                    print("Congrats! You win this round.")
                    print(f"Sum of your dices: {your_first_dice + your_second_dice} is higher than sum of his dices: {his_first_dice + his_second_dice}")
                else:
                    print("Pity! You lose this round.")
                    print(f"Sum of your dices: {your_first_dice + your_second_dice} is lower than sum of his dices: {his_first_dice + his_second_dice}")
                break
            else:
                print("OperatorError !!! write operator again.")
            break    
def dices():
     return [1,2,3,4,5,6]




while True:
    your_first_dice = random.choice(dices())
    your_second_dice = random.choice(dices())
    his_first_dice = random.choice(dices())
    his_second_dice = random.choice(dices())
    your_command = input("\n Write command 'To threw' for playing:\n")
    algoritm_of_game(your_first_dice, your_second_dice, his_first_dice, his_second_dice)
