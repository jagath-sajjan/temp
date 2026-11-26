import socket

while True:
  domain = input("Enter domain name: ")

  if domain == "exit":
    break

  try:
    ip = socket.gethostbyname(domain)
    print("IP address: ", ip)

  except:
    print("domain not found")
