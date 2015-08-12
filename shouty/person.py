class Person:
    def __init__(self, name, postman):
        self.messages_received = []
        self.name = name
        self.postman = postman

    def shout(self, message):
        self.postman.deliver(message, self.geo_location)

    def hear(self, message):
        self.messages_received.append(message)
