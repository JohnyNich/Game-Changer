import sys
import os
import time
import random
import os
games = ["blackjack"]
startup = True
pick_again = "yes"
def clear():
	os.system("clear")
def word_by_word(sentence):
	for letter in sentence:
		print(letter, end="")
		sys.stdout.flush()
		time.sleep(0.1)
	print ("")
def center_text(string):
	terminal_size = os.get_terminal_size()
	spaces = (terminal_size.columns - len(string)) / 2
	print (" " * int(spaces), end = "")
	word_by_word(string)
clear() # This is here just so that, if there's some text already on the termianl for some reason, it's gone.
while True:
	if startup == True:
		game = input("Welcome to Luck or Logic. Please choose a game to play. Type games to see what games there are available. Type exit to exit. \n")
		startup = False
	else:
		game = input("What do you want to do? \n")
	game = game.lower()
	if game == "blackjack":
		os.system("clear")
		center_text("Welcome to Blackjack")
		word_by_word("In this game, you will be given 2 cards, each can be from either 1 to 11.")
		word_by_word("The total of these two cards is your score. The goal of the game is for you to get the number closest to 21 versus your oponent.")
		word_by_word("But, if your number is over 21, then you loose.")
		word_by_word("After you have received 2 cards, you can choose if you want to pick up another one.")
		word_by_word("OK. Let's begin.")
		clear()
		while True:
			player_score = random.randint(1, 11) + random.randint(1, 11)
			computer_score = random.randint(1, 11) + random.randint(1, 11)
			word_by_word("Your score is " + str(player_score))
			while pick_again == "yes":
				word_by_word("Do you want to pick up another card?")
				pick_again = input("")
				pick_again = pick_again.lower()
				while pick_again != "yes" and pick_again != "no":
					word_by_word("Please enter either yes or no")
				if pick_again == "yes":
					new_card = random.randint(1, 11)
					word_by_word("Your new card is " + str(new_card))
					player_score += new_card
					word_by_word("Your total score is now " + str(player_score))
					if player_score > 21:
						break
			while True:
				difference = 21 - computer_score
				chance = difference / 19 # The smallest score you can get is 2, and the difference between 2 and 21 is 19. So the chance of failiure if the computer picks another card is calculated n / 19
				chacne = chance * 100
				if chacne <= 50:
					computer_score += random.randint(1, 11)
				else:
					break
			if player_score > 21:
				if computer_score > 21:
					word_by_word("Sorry. Your score is over 21. But the computer also got more than 21. It's a draw")
					result = "draw"
				else:
					word_by_word("Sorry. You lost. You score is over 21.") 
					result = "loss"
			else:
				if computer_score > 21:
					word_by_word("It seems that the computer's score is over 21. You win!")
					result = "win"
				elif player_score > computer_score:
					word_by_word("You win! You got a higher score than the computer!")
					result = "win"
				elif computer_score > player_score:
					word_by_word("The computer got a higher score than you. You lose.")
					result = "loss"
				elif player_score == computer_score:
					word_by_word("You both got the same score. It's a draw.")
	elif game == "games":
		print (games)
	elif game == "exit":
		sys.exit()
	else:
		print ("That's not a valid operation")

