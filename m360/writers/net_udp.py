import asyncio
import socket
from asyncio import sleep as asleep
from uuid import getnode

#influx: JMCZPhPz4h_LqhW1c7u2ndcegZaNTdaxf8Qzf15NSM0fxy4w-GjHAJcDyRcEctnkxVpLNGvQZB9_ALG88ooQOw==
broadcast_host = '255.255.255.255'
broadcast_port = 8888
node_id=getnode()
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
async def co(mtab={}):
    try:
        while True:
            for k,v in mtab:
                data = bytes(f"{node_id}|{k}|{v}")
                udp_socket.sendto(data, (broadcast_host, broadcast_port))
            await asleep(1)
    except Error as e:
        print(e)

def co_cleanup():
    udp_socket.close()
