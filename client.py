import socket
import subprocess
ping = []
host = "127.0.0.1"
porta = 65000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((host,porta))
	ping = subprocess.call("ping -c 3 8.8.8.8 > test.txt; date >> test.txt", shell="True")
	#s.sendall(b"Success! NICE KRAIO")
	#data = s.recv(1024)
	file = "/home/joaofth/Desktop/python/test.txt"
	fileo = open(file, "rb")
	envia = fileo.read(1024)
	s.sendall(envia)
	fileo.close()
print("Sucesso!")#, repr(data))