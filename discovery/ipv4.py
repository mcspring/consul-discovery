"""
Utils
"""

import socket

def get_ipv4():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 53))

        ipv4 = s.getsockname()[0]
    except Exception:
        ipv4 = socket.gethostbyname(socket.gethostname())
    finally:
        sock.close()

    return ipv4
