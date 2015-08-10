class Person:
    def __init__(self, network):
        self.network = network

    def shout(self, message):
        self.network.broadcast(message)
        pass

    def messages_heard(self):
        return []
