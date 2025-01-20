from rooms import Room

class Client:
    def __init__(self, id, jwt, public_key, socket):
        self.id = id
        self.jwt = jwt
        self.public_key = public_key
        self.socket = socket
        self.room = None

    def join_room(self, room: Room):
        self.room = room
        room.add_client(self)
