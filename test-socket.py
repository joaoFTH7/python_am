import socket

print("IP..:", socket.gethostbyname("www.google.com"))

dns_how = socket.getfqdn("8.8.8.8")
print(dns_how)
