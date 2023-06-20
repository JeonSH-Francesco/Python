import socket
import requests

hostname=socket.gethostname()
internal_ip = socket.gethostbyname(hostname)

response = requests.get('https://ipinfo.io/ip')
external_ip = response.text.strip()

print("내부 IP =",internal_ip)
print("외부 IP =", external_ip)
