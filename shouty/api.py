# from shouty.network import Network

class Api:

    MESSAGE_RANGE=1000

    def __init__(self):
        self.locations_by_shouter = {}
        self.shouts_by_shouter = {}
        pass

    def set_location(self, person, coordinate):
        self.locations_by_shouter[person] = coordinate

    def shout(self, shouter, message):
        if( not shouter in self.shouts_by_shouter ):
            self.shouts_by_shouter[shouter] = []
        self.shouts_by_shouter[shouter].append(message)

    def get_shouts_heard_by(self, listener):
        shouts_heard = {}
        for shouter, shouts in self.shouts_by_shouter.items():
            shouter_location = self.locations_by_shouter[shouter]
            listener_location = self.locations_by_shouter[listener]

            if (shouter_location.distance_from(listener_location) < self.MESSAGE_RANGE):
                shouts_heard[shouter] = shouts
        return shouts_heard
