import socket
import threading

# Настройки
HOST = '0.0.0.0'  # Слушаем все интерфейсы
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} ливнул!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    print(f"Сервер запущен на порту {PORT}...")
    while True:
        client, address = server.accept()
        print(f"Коннект с {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Никнейм клиента: {nickname}")
        broadcast(f"{nickname} зашел в чат!".encode('utf-8'))
        client.send('Подключено к серверу!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
