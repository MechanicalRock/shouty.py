from shouty.person import Person
from shouty.postman import Postman

class Api:
    def __init__(self):
        self.people = {}
        self.postman = Postman()

    def person_is_at_geo_location(self, person_name, geo_location):
        person = self._find_or_create_person(person_name)
        person.geo_location = geo_location

    def person_shouts_message(self, person_name, message):
        person = self._find_or_create_person(person_name)
        person.shout(message)

    def messages_heard_by(self, person_name):
        person = self._find_or_create_person(person_name)
        return person.messages_received

    def _find_or_create_person(self, person_name):
        if person_name not in self.people:
            self.people[person_name] = Person(self.postman)
        return self.people[person_name]
