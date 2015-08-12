from shouty.person import Person
from shouty.postman import Postman

class Api:
    def __init__(self):
        self.postman = Postman()

    def person_is_at_geo_location(self, person_name, geo_location):
        person = self.postman.find_or_create_person(person_name)
        person.geo_location = geo_location

    def person_shouts_message(self, person_name, message):
        person = self.postman.find_or_create_person(person_name)
        person.shout(message)

    def messages_heard_by(self, person_name):
        person = self.postman.find_or_create_person(person_name)
        return person.messages_received
