#from shouty.network import Network
from shouty.person import Person

class Api:
    def __init__(self):
        self.people = {}

    def person_is_at_geo_location(self, person_name, geo_location):
        person = self._find_or_create_person(person_name)
        person.geo_location = geo_location

    def person_shouts_message(self, person_name, message):
        pass

    def messages_heard_by(self, person_name):
        return []

    def _find_or_create_person(self, person_name):
        if person_name not in self.people:
            self.people[person_name] = Person()
        return self.people[person_name]
