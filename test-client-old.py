import socket
import subprocess

host = ''
port = 65000


ip = input("Digite o IP..: ")
addr = (ip,port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

mensagem = input("Digite a sua mensagem..: ")

client_socket.send(mensagem.encode("utf-8"))
print("Mensagem enviada!")
#testes para receber shell
#f mensagem == 's':
#recebe = conn.recv(1024)
client_socket.close()
