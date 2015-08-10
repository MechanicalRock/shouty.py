from shouty.person import Person
from haversine import haversine

class Network:
    def __init__(self):
        self.people = {}

    def find_or_create_person(self, person_name):
        if (person_name not in self.people):
            self.people[person_name] = Person(self)
        return self.people[person_name]

    def broadcast(self, message, shout_geo_location):
        for listener in self.people.itervalues():
            if (self._in_range(shout_geo_location, listener.geo_location)):
                listener.hear(message)

    def _in_range(self, loc1, loc2):
        return haversine(loc1, loc2) <= 1.0 # 1km = 1000m
