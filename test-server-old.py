import socket
import subprocess
host = '0.0.0.0'
port = 65000
addr = (host,port)

serv_socketa = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_socketa.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serv_socketa.bind(addr)

serv_socketa.listen(1)


print("Aguardando Conexão..") 

conn, cliente = serv_socketa.accept()
print("Conexão estabelecida!")
print("Aguardando mensagem..: ")

file = "/home/joaofth/test.txt"
fileo = open(file, "wb")
fileo.write(conn.recv(1024))
fileo.close()
#recebe = conn.recv(1024)

#print("Mensagem recebida..: ", recebe)
#testes para enviar shell para o cliente
#if recebe == "s".encode("utf-8"):
#	serv_socketa.send(subprocess.call("sh", shell='True'))

#serv_socketa.close()