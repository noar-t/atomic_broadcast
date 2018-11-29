from channel import Channel

class Atomic_Broadcaster(object):

    def __init__(self, hosts, ports):
        self.channels = [Channel(hosts, p) for p in ports]

    # Send message on all channels
    def broadcast(self, message):
        for c in self.channels:
            c.broadcast(message)



class Message(object):
    def __init__(self, host, data):
        self.time = None #TODO i think it might be best to only set time right
                         # before message is sent to be most accurate
        self.hops = 1
        self.origin = host
        self.data = data

    def add_hop(self):
        self.hops += 1
