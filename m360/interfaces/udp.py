
import asyncio

async def udp_server():
    # Create a UDP server socket
    udp_socket = await asyncio.start_server(handle_client, '0.0.0.0', 8888, family=socket.AF_INET, proto=socket.IPPROTO_UDP)

    async with udp_socket:
        await udp_socket.serve_forever()

async def handle_client(reader, writer):
    data, addr = await reader.read(1024)
    message = data.decode()
    print(f"Received {message} from {addr}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(udp_server())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
