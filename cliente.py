import socket

def iniciar_cliente():
    # Crear el socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar con el servidor. Aquí el sistema operativo hace
    # automáticamente el TCP 3-way handshake (SYN, SYN-ACK, ACK).
    cliente_socket.connect(('127.0.0.1', 8080))
    print("[*] Conexión TCP establecida con el servidor.")

    # Enviar una petición HTTP, como lo hace un navegador web.
    peticion_http = "GET / HTTP/1.1\r\nHost: 127.0.0.1:8080\r\n\r\n"
    cliente_socket.sendall(peticion_http.encode('utf-8'))
    print("[*] Petición HTTP enviada.")

    # Recibir la respuesta del servidor (HTML).
    respuesta = cliente_socket.recv(1024).decode('utf-8')
    print("--- Respuesta recibida del servidor ---")
    print(respuesta)

    # Cerrar la conexión.
    cliente_socket.close()
    print("[*] Conexión cerrada por el cliente.")

if __name__ == "__main__":
    iniciar_cliente()
