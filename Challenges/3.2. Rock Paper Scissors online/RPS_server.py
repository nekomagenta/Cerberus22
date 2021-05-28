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

close = False
while close == False:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind(HOST_PORT)
		s.listen()
		conn, addr = s.accept()
		with conn:
			print('Connected by', addr)
			while True:
				data = conn.recv(1024)
				if not data:
					break
				if data == b'close':
					conn.sendall(b'Closing server.')
					quit()

				