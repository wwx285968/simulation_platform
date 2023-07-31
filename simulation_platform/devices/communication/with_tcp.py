import socket
import select

from simulation_platform.devices.communication.base import Commucation


class TcpComm(Commucation):
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        self.sock.connect((self.ip, self.port))

    def receive_cmd(self):
        read_sockets, _, _ = select.select([self.sock], [], [], self.timeout)
        if read_sockets:
            sock = read_sockets[0]
            try:
                data = sock.recv(1024)
                if data:
                    return data
            except socket.error as e:
                _ = e
                self.sock.close()

    def report_state(self):
        pass
