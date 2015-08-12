from haversine import haversine
from shouty.person import Person

class Postman:
    def __init__(self):
        self.people = {}

    def deliver(self, message, geo_location):
        for listener in self.people.values():
            if self._within_range(geo_location, listener.geo_location):
                listener.hear(message)

    def find_or_create_person(self, person_name):
        if person_name not in self.people:
            self.people[person_name] = Person(person_name, self)
        return self.people[person_name]

    def _within_range(self, loc1, loc2):
        return haversine(loc1, loc2) <= 1.0 # 1km
