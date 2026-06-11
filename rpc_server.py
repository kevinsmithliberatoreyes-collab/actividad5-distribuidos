
from xmlrpc.server import SimpleXMLRPCServer

# Función remota que será llamada por el cliente
def calcular_cuadrado(numero):
    print(f"[*] Solicitud recibida. Calculando el cuadrado de: {numero}")
    return numero * numero

def iniciar_rpc_servidor():
    # Se levanta el servidor RPC en el puerto 8000
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("[*] Servidor RPC escuchando en el puerto 8000...")
    
    # Se registra la función para que los clientes puedan acceder a ella
    server.register_function(calcular_cuadrado, "calcular_cuadrado")
    server.serve_forever()

if __name__ == '__main__':
    iniciar_rpc_servidor()
