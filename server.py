import socket

HOST = "127.0.0.1"
PORT = 5000


def process_message(message):
    """
    Simulates a server processing a valid request.

    In this demonstration, the server does NOT use:
    - timestamps
    - nonces
    - sequence numbers
    - replay detection

    Therefore, the same valid message can be processed repeatedly.
    """

    print(f"[SERVER] Processing request: {message}")

    if message.startswith("ACCESS|"):
        parts = message.split("|")

        if len(parts) == 3:
            user = parts[1]
            resource = parts[2]

            print(
                f"[SERVER] Access granted to {user} "
                f"for resource: {resource}"
            )

            return "ACCESS GRANTED"

    return "INVALID MESSAGE"


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(5)

    print("===================================")
    print("       REPLAY ATTACK LAB")
    print("===================================")
    print(f"[SERVER] Listening on {HOST}:{PORT}")
    print("[SERVER] Waiting for clients...\n")

    try:

        while True:

            conn, addr = server.accept()

            print(f"[SERVER] Connection from {addr}")

            while True:

                data = conn.recv(1024)

                if not data:
                    break

                message = data.decode()

                print(f"[SERVER] Received: {message}")

                response = process_message(message)

                conn.send(response.encode())

            conn.close()

            print("[SERVER] Connection closed.\n")

    except KeyboardInterrupt:

        print("\n[SERVER] Server stopped.")

    finally:

        server.close()


if __name__ == "__main__":
    start_server()
