import sys
from dataclasses import dataclass


def retrieve_sockets():
    if sys.platform == 'win32':
        print("win32")
        return # window socket transport
    if sys.platform == 'darwin':
        print("macos")
        return #macos socket transport
    if sys.platform == 'linux':
        print("macos")
        return #linux socket transport
    else:
        raise NotImplementedError('Unsupported platform: {}'.format(sys.platform))

@dataclass
class Endpoint:
    socket: socket.socket
    path: str
