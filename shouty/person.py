class Person:
    def __init__(self, network):
        self.network = network
        self.messages_heard = []
        self.geo_location = [0,0]

    def shout(self, message):
        self.network.broadcast(message, self.geo_location)
        pass

    def hear(self, message):
        self.messages_heard.append(message)
