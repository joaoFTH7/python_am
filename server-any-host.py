import socket
import subprocess

host = "0.0.0.0"
porta = 65000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((host,porta))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print("Conectado com ", addr)
		#recebe = conn.recv(1024)
		#print(recebe)
		while True:
			data = conn.recv(1024)
			#mostrar o que está sendo recebido
			print(data)
			#bloco para interromper a chegada de dados
			if not data:
				break
			conn.sendall(data)





