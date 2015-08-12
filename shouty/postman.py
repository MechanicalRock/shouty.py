from haversine import haversine

class Postman:
    def __init__(self):
        self.people = []

    def subscribe(self, person):
        self.people.append(person)

    def deliver(self, message, geo_location):
        for listener in self.people:
            if self._within_range(geo_location, listener.geo_location):
                listener.hear(message)

    def _within_range(self, loc1, loc2):
        return haversine(loc1, loc2) <= 1.0 # 1km
