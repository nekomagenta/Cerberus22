print("""
 __  __           _        _           
|  \/  | __ _  __| | ___  | |__  _   _ 
| |\/| |/ _` |/ _` |/ _ \ | '_ \| | | |
| |  | | (_| | (_| |  __/ | |_) | |_| |
|_|  |_|\__,_|\__,_|\___| |_.__/ \__, |
                                 |___/ 
     ________  ________  ______   ________  ________  ______   __    __  ________
    /  _____/ /  _____/ /  __  \ /  __   / /  _____/ /  __  \ /  /  /  //  _____/
   /  /      /  /____  /  /_/  //  /_/  / /  /____  /  /_/  //  /  /  //  /_____
  /  /      /  _____/ /  __  _//   __   //   ____/ /  __  _//  /  /  //_____   /
 /  /_____ /  /_____ /  / / \ /   /_/  //   /____ /  / / \ /  /__/  //_____/  /
/________//________//__/ /__//________//________//__/ /__//________//________/
""")
import socket

rps = ['rock', 'paper', 'scissors']

HOST_PORT = ('127.0.0.1', 4344)

choice = ''
def get_choice():
	global choice
	choice = input("Rock, paper or scissors? ").lower()

get_choice()
while choice not in rps:
	print("Invalid option, please try again.")
	get_choice()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect(HOST_PORT)
	s.sendall(choice.encode('utf-8'))
	data = s.recv(1024)

print(data.decode('utf-8'))