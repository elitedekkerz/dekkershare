import socket
import time
import json
import threading

class peer_handler():

    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.connection.settimeout(0)
        self.connection.bind(('',42069))

        self.update_interval = 60
        self.timeout = 60*5
        self.peers = {}
        self.thread_run = True
        """
        {
        "127.0.0.0":{
            "timestamp":53925923
            }
        }
        """

    def send_peers_message(self,message):
        """
        send given message as json encoded packet
        """
        self.connection.sendto(json.dumps(message).encode(),('<broadcast>',42069))

    def announce(self):
        """
        broadcast a signal for peer clients to know our presence
        """
        self.send_peers_message({"message":"announce"})

    def handle_peer_messages(self):
        """
        handle peer messages
        """
        #messages = []
        while True:
            try:
                data_raw, addr = self.connection.recvfrom(1024)
            except BlockingIOError:
                break

            #check that the data is in a format we can use
            try:
                data = json.loads(data_raw.decode())
            except:
                print(data_raw)

            peer_key = addr[0]

            #update whatever data is given
            self.peers.update({peer_key:data})

            if data['message'] == 'announce':
                #update peer timestamp
                self.peers[peer_key]["timestamp"] = time.time()

    def get_valid_peers(self):
        """
        return a new list without expired peers
        """
        new_peers = {}
        for peer in self.peers.keys():
            
            if self.peers[peer]['timestamp'] < time.time() + self.timeout:
                new_peers.update({peer:self.peers[peer]})

        self.peers = new_peers

    def update_peers(self):
        """
        announce self to other peers and
        check for available peers
        """
        self.announce()
        self.handle_peer_messages()
        self.get_valid_peers()

        if self.thread_run:
            t  = threading.Timer(self.update_interval, self.update_peers)
            t.start()
