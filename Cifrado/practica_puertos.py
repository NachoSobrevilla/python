import socket

# Función para escanear un puerto específico
def scan_port(host, port):
    try:
        # Creamos un objeto socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Establecemos un tiempo de espera de conexión de 1 segundo
        s.settimeout(1)
        # Intentamos conectar al host y puerto especificados
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"El puerto {port} está abierto")
        else:
            print(f"El puerto {port} está cerrado")
        # Cerramos la conexión
        s.close()
    except socket.error:
        print(f"No se pudo conectar al puerto {port}")

# Función para escanear un rango de puertos
def scan_ports(host, start_port, end_port):
    print(f"Escaneando puertos en {host}...")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

# Ingresa el host que deseas escanear (puede ser 'localhost' para escanear tu propia computadora)
host = input("Ingresa el host que deseas escanear: ")
# Ingresa el rango de puertos que deseas escanear
start_port = int(input("Ingresa el puerto de inicio: "))
end_port = int(input("Ingresa el puerto final: "))

# Llamamos a la función para escanear los puertos
scan_ports(host, start_port, end_port)