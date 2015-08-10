from shouty.person import Person

class Network:
    def __init__(self):
        self.people = {}

    def find_or_create_person(self, person_name):
        if (person_name not in self.people):
            self.people[person_name] = Person(self)
        return self.people[person_name]

    def broadcast(self, message):
        for listener in self.people.itervalues():
            listener.hear(message)
