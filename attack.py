import socket
import time

HOST = "127.0.0.1"
PORT = 5000

# This represents a previously captured valid message.
#
# The attacker does not need to create a new valid message.
# The attacker simply reuses the exact same message.
REPLAYED_MESSAGE = "ACCESS|student01|NETWORK_LAB"


def attack():

    print("===================================")
    print("        REPLAY ATTACK SIMULATOR")
    print("===================================")

    print("\n[ATTACKER] Previously captured message:")
    print(f"[ATTACKER] {REPLAYED_MESSAGE}")

    time.sleep(1)

    attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    attacker.connect((HOST, PORT))

    print(f"\n[ATTACKER] Connected to {HOST}:{PORT}")

    print("\n[ATTACKER] Replaying the captured message...")

    attacker.send(REPLAYED_MESSAGE.encode())

    response = attacker.recv(1024).decode()

    print(f"[ATTACKER] Server response: {response}")

    attacker.close()

    print("\n[ATTACKER] Replay completed.")


if __name__ == "__main__":
    attack()
