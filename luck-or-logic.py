import sys
import os
import time
games = ["blackjack"]
startup = True
def clear():
	os.system("clear")
def word_by_word(sentence):
	for letter in sentence:
		print(letter, end="")
		sys.stdout.flush()
		time.sleep(0.1)
	print ("")
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
		word_by_word("Welcome to Blackjack. In this game, you will be given 2 numbers, each can be from either 1 to 11.")
		word_by_word("The total of these two numbers is your score. The goal of the game is for you to get the number closest to 21 versus your oponent.")
		word_by_word("But, if your number is over 21, then you loose.")
		word_by_word("After you have received 2 cards, you can choose if you want to pick up another one.")
		word_by_word("OK. Let's begin.")
		clear()
	elif game == "games":
		print (games)
	elif game == "exit":
		sys.exit()
	else:
		print ("That's not a valid operation")

