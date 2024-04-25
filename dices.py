#Dice game
import random


def dices():
     return [1,2,3,4,5,6]





    






def algoritm_of_game(your_command, your_first_dice, your_second_dice, his_first_dice, his_second_dice, your_balance, his_balance):
            if your_command.lower() == "to threw":    
                
                if your_first_dice + your_second_dice == his_first_dice + his_second_dice:
                    print("It is tie.")
                    your_balance -= 1
                    print(f"Your balance is equal to {your_balance}")
                    his_balance -= 1
                    print(f"his balance is equal to {your_balance}")
                    print(f"Sum of your dices: {your_first_dice + your_second_dice} is equal to the sum of his dices: {his_first_dice + his_second_dice}")
                if your_first_dice + your_second_dice > his_first_dice + his_second_dice:
                    print("Congrats! You win this round.")
                    your_balance += (your_first_dice + your_second_dice)
                    print(f"Your balance is equal to {your_balance}.")
                    his_balance -= (your_first_dice + your_second_dice)
                    print(f"Sum of your dices: {your_first_dice + your_second_dice} is higher than sum of his dices: {his_first_dice + his_second_dice}")
                else:
                    print("Pity! You lose this round.")
                    your_balance -= (his_first_dice + his_second_dice)
                    print(f"Your balance is equal to {your_balance}.")
                    his_balance += (his_first_dice + his_second_dice)
                    print(f"Sum of your dices: {your_first_dice + your_second_dice} is lower than sum of his dices: {his_first_dice + his_second_dice}")
            else:
                print("OperatorError !!! write operator again.")
                




# Your dices

your_first_dice = random.choice(dices())
your_second_dice = random.choice(dices())


# His dices

his_first_dice = random.choice(dices())
his_second_dice = random.choice(dices())


# his balance

his_balance = 100


# your balance

your_balance = 100


# Your comand

your_command = input("\n Write command 'To threw' for playing:\n")


algoritm_of_game(your_command, your_first_dice, your_second_dice, his_first_dice, his_second_dice, your_balance, his_balance)
