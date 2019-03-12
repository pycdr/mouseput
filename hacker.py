from socket import socket
#==========================#
s = socket()
host = input("~ target ip: ")
port = int(input("~ target port: "))
s.connect((host,port))
#==========================#
while 1:
	t = input(
"""[
	1) control with moving your mouse :)
	2) get input and send position
] which one[1,2]? """)
	if t not in {"1","2"}:
		print("~ just type 1 or 2.")
		continue
	break
#==========================#
print("~ start...")
try:
	if t == "1":
		import pyautogui as g
		while 1:
			pos = g.position()
			d = str(pos[0])+","+str(pos[1])
			s.sendall(d.endoce("utf8"))
			d = s.recv(1024)
			d = d.decode("utf8")
			if d == "0":
				print("~ error in set target mouse position!")
				if input("~ continue[y=yes/other=no]?") == "y":
					continue
				break
			elif d == "1":
				print("~ fine!")
		s.close()
	else:
		while 1:
			print("pos:")
			d = input("\tx:")+","+input("\ty:")
			s.sendall(d.encode("utf8"))
			d = s.recv(1024)
			d = d.decode("utf8")
			if d == "0":
				print("~ error in set target mouse position!")
				if input("~ continue?") == "y":
					continue
				break
			elif d == "1":
				print("~ fine!")

except KeyboardInterrupt:
	print("~ by..!")
finally:
	s.close()
