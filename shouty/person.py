class Person:
    def __init__(self, postman):
        self.messages_received = []
        self.postman = postman
        postman.subscribe(self)

    def shout(self, message):
        self.postman.deliver(message, self.geo_location)

    def hear(self, message):
        self.messages_received.append(message)
