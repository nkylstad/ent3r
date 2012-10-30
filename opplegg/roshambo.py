# Uke 9, oppg 9.3, ninakky: roshambo.py
import random

def paper(opponent):
	if opponent=="p":
		return 0
	elif opponent=="s":
		return -1
	else:
		return 1

def scissors(opponent):
	if opponent=="s":
		return 0
	elif opponent=="r":
		return -1
	else:
		return 1

def rock(opponent):
	if opponent=="r":
		return 0
	elif opponent=="p":
		return -1
	else:
		return 1

choices = {"p": "paper", "s": "scissors", "r": "rock"}
options = {"p": paper, "s": scissors, "r": rock}

def play(human, computer):
	player_choice = raw_input("Choose (r)ock, (p)aper or (s)cissors:  ")
	program_choice = random.choice(options.keys())
	try:
		winner = options[program_choice](player_choice)
		print "Human: ", choices[player_choice], "   Computer: ", choices[program_choice]
		if winner < 0: 
			print "Player wins!"
			human += 1
		elif winner > 0: 
			print "Computer wins!"
			computer += 1
		else: print "Draw!"
		print " "
	except:
		print "Please choose rock (r), paper (p), or scissors (s)."
	return human, computer


def opening_statements():
	print "Welcome to Rock, Paper, Scissors!"
	print " "
	win_points = float(raw_input("How many points are required for a win?  "))
	#win_points = float(raw_input("How many times shall we play?  "))
	return win_points


points = opening_statements()
i = 0
human = 0
computer = 0
while human<points and computer<points:
	print "Score: Human %d   Computer %d" % (human, computer)
	human, computer = play(human, computer)
	i+=1

print "Final score: Human %d    Computer %d" %(human, computer)