import requests

def get_ip():
    response = requests.get('https://ifconfig.me/ip')
    return response.text.strip()


public_ip = get_ip()
if public_ip:
    print(f'Текущий публичный IP-адрес: {public_ip}')
