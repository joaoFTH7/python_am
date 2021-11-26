import socket
import subprocess
import time
from crontab import CronTab



#while True:

cron = CronTab(user='joaofth')
job = cron.new(command="python3 /home/joaofth/Desktop/python/ipv6/cron-test.py")
job.minute.every(1)
cron.write()
cron.remove(job)
cron.remove_all()
cron.write()
addr = ("127.0.0.1",65000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((addr))
msg = "It's Alive"
client_socket.send(msg.encode("utf-8"))
print("Mensagem enviada!")
client_socket.close()
time.sleep(15)