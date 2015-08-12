from haversine import haversine

STANDARD_SHOUT_DISTANCE = 1.0

class Person:
    def __init__(self, name, postman):
        self.geo_location = [0,0]
        self.messages_received = []
        self.name = name
        self.postman = postman

    def shout(self, message):
        self.postman.deliver(message, self)

    def hear(self, message):
        self.messages_received.append(message)

    def within_range(self, geo_location):
        return haversine(self.geo_location, geo_location) <= STANDARD_SHOUT_DISTANCE
