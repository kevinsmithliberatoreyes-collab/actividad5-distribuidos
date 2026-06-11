import socket

def iniciar_servidor():
    host = '127.0.0.1'
    puerto = 65432

    # Se crea el socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, puerto))
        s.listen()
        print(f"[*] Servidor Socket en espera de conexiones en {host}:{puerto}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"[*] Conectado exitosamente por {addr}")
            data = conn.recv(1024)
            print(f"[Mensaje recibido del cliente]: {data.decode('utf-8')}")
            
            # Responder con confirmación
            respuesta = "Mensaje recibido correctamente. ¡Confirmación exitosa!"
            conn.sendall(respuesta.encode('utf-8'))

if __name__ == '__main__':
    iniciar_servidor()
