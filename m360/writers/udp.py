import asyncio
import socket
from asyncio import sleep as asleep
from uuid import getnode

#influx: JMCZPhPz4h_LqhW1c7u2ndcegZaNTdaxf8Qzf15NSM0fxy4w-GjHAJcDyRcEctnkxVpLNGvQZB9_ALG88ooQOw==
broadcast_host = '255.255.255.255'
broadcast_port = 8888
node_id=getnode()
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
async def co(mtab={}):
    sk = list(mtab.keys())
    sk.sort()
    try:
        while True:
            for k in sk:
                v = mtab[k]
                data = bytes(f"{node_id}|{k}|{v}", "ascii")
                udp_socket.sendto(data, (broadcast_host, broadcast_port))
            await asleep(1)
    except Exception as e:
        print(e)

def co_cleanup():
    udp_socket.close()
