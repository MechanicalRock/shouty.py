from shouty.network import Network

class Api:
    def __init__(self):
        self.network = Network()

    def person_is_at(self, person_name, geo_location):
        person = self.network.find_or_create_person(person_name)
        person.geo_location = geo_location

    def person_shouts(self, person_name, message):
        person =self.network.find_or_create_person(person_name)
        person.shout(message)

    def messages_heard_by(self, person_name):
        person = self.network.find_or_create_person(person_name)
        return person.messages_heard
