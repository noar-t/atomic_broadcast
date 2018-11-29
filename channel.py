# Since there is no access to creating and setting up multicast groups on
# UTCS routers we will spew the UDP packets to all hosts manually
import socket

class Channel(object):

    def __init__(self, hosts, port):
        self.hosts = hosts
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((socket.gethostname(), self.port))

    def broadcast(self, message):
        for host in self.hosts:
            self.socket.sendto(message, (host, self.port))

    # TODO probably need to switch to processes in order to use blocking
    # this way no messages can be lost
    def recv(self):
        data, _ = self.socket.recvfrom(1024)
        buf = data
        while data:
            data, _ = self.socket.recvfrom(1024)
            buf += data

        return buf
