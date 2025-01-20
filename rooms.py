from client import Client

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)
