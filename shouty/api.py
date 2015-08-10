from shouty.person import Person

class Api:
    def __init__(self):
        self.people = {}

    def person_is_at(self, person_name, geo_location):
        person = self._find_or_create_person(person_name)
        person.geo_location = geo_location

    def person_shouts(self, person_name, message):
        person = self._find_or_create_person(person_name)
        person.shout(message)

    def messages_heard_by(self, person_name):
        person = self._find_or_create_person(person_name)
        return person.messages_heard()

    def _find_or_create_person(self, person_name):
        if (person_name not in self.people):
            self.people[person_name] = Person()
        return self.people[person_name]
