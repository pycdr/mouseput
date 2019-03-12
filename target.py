import socket,os,sys
import pyautogui as gui
s = socket.socket()
def get_ip():
	if sys.platform in ("linux","darwin"):
		return os.popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'").read()
	#elif sys.platform in ("win32","cygwin"):
	else:
		si = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		si.connect(("8.8.8.8", 80))
		si.close()
		return s.getsockname()[0]
try:
	s.bind((get_ip(),6969))
	s.listen(1)
	h = s.accept()
	while 1:
		d = h[0].recv(1024)
		d = str(d)[2:-1].split(",")
		if len(d) != 2:
			h[0].sendall(b"0")
			break
		try:
			gui.moveTo(int(d[0]),int(d[1]))
			h[0].sendall(b"1")
		except:
			h[0].sendall(b"0")
except:
	pass
s.close()
