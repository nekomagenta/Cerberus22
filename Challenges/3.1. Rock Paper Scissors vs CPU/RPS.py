import random
player_choice, cpu_choice = "", ""
rps = ['rock', 'paper', 'scissors']

print("""
     ________  ________  ______   ________  ________  ______   __    __  ________
    /  _____/ /  _____/ /  __  \ /  __   / /  _____/ /  __  \ /  /  /  //  _____/
   /  /      /  /____  /  /_/  //  /_/  / /  /____  /  /_/  //  /  /  //  /_____
  /  /      /  _____/ /  __  _//   __   //   ____/ /  __  _//  /  /  //_____   /
 /  /_____ /  /_____ /  / / \ /   /_/  //   /____ /  / / \ /  /__/  //_____/  /
/________//________//__/ /__//________//________//__/ /__//________//________/
""")


def get_choices():
	global player_choice, cpu_choice
	cpu_choice = rps[random.randint(0, len(rps)-1)]
	player_choice = input("Rock, paper or scissors? ").lower()

get_choices()
while player_choice not in rps:
	print("Invalid option, please try again.")
	get_choices()

def player_win():
	print(f"You won! CPU chose {cpu_choice}, player chose {player_choice}")
	quit()

def player_lose():
	print(f"You lost! CPU chose {cpu_choice}, player chose {player_choice}")
	quit()

while True:
	if player_choice == cpu_choice:
		print(f"It's a tie! Both players chose {cpu_choice}. \nTry again!")
		get_choices()
	elif player_choice == 'rock':
		if cpu_choice == 'paper':
			player_lose()
		elif cpu_choice == 'scissors':
			player_win()

	elif player_choice == 'paper':
		if cpu_choice == 'rock':
			player_win()
		elif cpu_choice == 'scissors':
			player_lose()
	elif player_choice == 'scissors':
		if cpu_choice == 'paper':
			player_win()
		elif cpu_choice == 'rock':
			player_lose()
