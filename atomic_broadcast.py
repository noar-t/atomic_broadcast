import multiprocessing as mp
from channel import Channel, Message

class AtomicBroadcaster(object):

    def __init__(self, hosts, ports):
        self.channels = [Channel(hosts, port) for port in ports]
        self.__forwarder = mp.Process(target=self.__forwarder_worker,
                                      daemon=True)
        self.__forwarder.start()

    def __forwarder_worker(self):
        pass


    # Send message on all channels
    def broadcast(self, message):
        for c in self.channels:
            c.broadcast(message)

