import xmlrpc.client

def iniciar_rpc_cliente():
    try:
        # Se solicita el número entero al usuario
        entrada = input("Introduce un número entero para calcular su cuadrado: ")
        numero = int(entrada)
        
        # Conexión al servidor RPC
        proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
        
        # Llamada a la función remota
        resultado = proxy.calcular_cuadrado(numero)
        print(f"[*] El cuadrado de {numero} devuelto por el servidor es: {resultado}")
        
    except ValueError:
        print("[Error]: Debes introducir un número entero válido.")
    except ConnectionRefusedError:
        print("[Error]: No se pudo conectar al servidor RPC. Verifica que esté corriendo.")

if __name__ == '__main__':
    iniciar_rpc_cliente()
