import socket

def iniciar_cliente():
    host = '127.0.0.1'
    puerto = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("[*] Conectando al servidor...")
        s.connect((host, puerto))
        
        mensaje = "Hola Servidor, este es un mensaje de prueba para la Actividad 5."
        s.sendall(mensaje.encode('utf-8'))
        print("[*] Mensaje enviado al servidor.")
        
        data = s.recv(1024)
        print(f"[Respuesta del servidor]: {data.decode('utf-8')}")

if __name__ == '__main__':
    iniciar_cliente()
