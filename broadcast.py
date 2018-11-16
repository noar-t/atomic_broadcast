
class Atomic_Broadcaster(object):

    def __init__(self, ports):
        self.ports = ports

    def broadcast(self):
        #TODO broadcast
        pass

class Message(object):
    def __init__(self, host, data):
        self.time = None #TODO i think it might be best to only set time right
                         # before message is sent to be most accurate
        self.hops = 1
        self.host = host
        self.data = data

    def add_hop(self):
        self.hops += 1
