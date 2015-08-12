from shouty.person import Person

class Postman:
    def __init__(self):
        self.people = {}

    def deliver(self, message, geo_location):
        for listener in self.people.values():
            if listener.within_range(geo_location):
                listener.hear(message)

    def find_or_create_person(self, person_name):
        if person_name not in self.people:
            self.people[person_name] = Person(person_name, self)
        return self.people[person_name]
