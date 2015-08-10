from shouty.person import Person
from nose.tools import assert_equals
from mock import Mock

def test_person_tells_network_to_broadcast():
    network = Mock()
    person = Person(network)
    person.shout("hello")
    network.broadcast.assert_called_once_with("hello")
