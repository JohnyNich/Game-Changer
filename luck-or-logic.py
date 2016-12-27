import sys
games = ["blackjack"]
startup = True
while True:
	if startup == True:
		game = input("Welcome to Luck or Logic. Please choose a game to play. Type games to see what games there are available. Type exit to exit. \n")
		startup = False
	else:
		game = input("What do you want to do? \n")
	game = game.lower()
	if game == "blackjack":
		pass
	elif game == "games":
		print (games)
	elif game == "exit":
		sys.exit()
	else:
		print ("That's not a valid operation")

