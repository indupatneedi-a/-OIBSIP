import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"   # localhost
PORT = 5555

clients = {}          # connection -> username
lock = threading.Lock()


def timestamp():
    return datetime.now().strftime("[%H:%M]")


def broadcast(message, sender=None):
    """Send a message to every connected client except the sender."""
    with lock:
        for conn in list(clients):
            if conn is not sender:
                try:
                    conn.sendall(message.encode("utf-8"))
                except OSError:
                    pass


def handle_client(conn):
    """Handle one client: read its name, then relay its messages."""
    try:
        name = conn.recv(1024).decode("utf-8").strip() or "Guest"
        with lock:
            clients[conn] = name
        print(f"{timestamp()} {name} joined the chat.")
        broadcast(f"{timestamp()} {name} joined the chat.\n", conn)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode("utf-8").strip()
            if message.lower() == "/quit":
                break
            broadcast(f"{timestamp()} {name}: {message}\n", conn)
    except (ConnectionResetError, OSError):
        pass
    finally:
        with lock:
            name = clients.pop(conn, None)
        conn.close()
        if name:
            print(f"{timestamp()} {name} left the chat.")
            broadcast(f"{timestamp()} {name} left the chat.\n")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, _ = server.accept()
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()


if __name__ == "__main__":
    start_server()
