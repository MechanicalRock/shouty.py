from shouty.network import Network
from mock import Mock

def test_network_broadcast_delivers_message_to_all_people():
    network = Network()
    lucy = Mock()
    network.people = {'Lucy': lucy}

    network.broadcast("hello")
    lucy.hear.assert_called_once_with("hello")
