import subprocess
#!/usr/bin/env python

comando = ""

#init = subprocess.call("echo '!/bin/sh -e init.d' > /etc/init.d/", shell="True")
comando = subprocess.call("ls /home/joaofth > /home/joaofth/Desktop/user_home.txt", shell="True")
comando = subprocess.call("date >> /home/joaofth/Desktop/user_home.txt", shell="True")
