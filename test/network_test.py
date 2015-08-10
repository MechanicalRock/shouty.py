from shouty.network import Network
from mock import Mock

leicester_square =  [51.5114242, -0.1287315]
piccadilly_circus = [51.5101210, -0.1341683]
heathrow =          [51.4715066, -0.4879044]

def test_network_broadcast_delivers_message_to_all_people_in_range():
    network = Network()
    lucy = Mock()
    lucy.geo_location = piccadilly_circus
    network.people = {'Lucy': lucy}

    network.broadcast("hello", leicester_square) # Leicester Square Station
    lucy.hear.assert_called_once_with("hello")

def test_network_broadcast_does_not_deliver_message_to_people_outside_range():
    network = Network()
    lucy = Mock()
    lucy.geo_location = piccadilly_circus
    network.people = {'Lucy': lucy}

    network.broadcast("hello", heathrow) # Leicester Square Station
    assert not lucy.hear.called
