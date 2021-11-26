import socket
import subprocess

host = ""
porta = 65000
entrar = "S"
comando = ""
#sem ipv6 para testes
while entrar == "S":	
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		#sem ipv6
		s.bind((host,porta))
		s.listen()
		conn, addr = s.accept()
		with conn:
			print("Conectado com ", addr)
			#recebe = conn.recv(1024)
			#print(recebe)
	#		while True:
			data = conn.recv(1024)
				#mostrar o que está sendo recebido
			print(data.decode("utf-8"))
				#bloco para interromper a chegada de dados
	#			if not data:
	#				break
			#conn.sendall(data)
			comando = input("Digite o comando..: ")
			conn.send(comando.encode("utf-8"))
			comando2 = conn.recv(1024)
			print(comando2.decode("utf-8"))
		entrar = input("Permanecer com o server no ar: S ou N..: ").upper()
		s.listen()