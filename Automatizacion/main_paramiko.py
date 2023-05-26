import paramiko
import time
import os

from getpass import getpass

HOST = "192.168.1.68"
USER = "sobr3s"

if __name__ == '__main__':
    #se hace ping al server
    ping_response = os.system(f"ping {HOST}")
    #Si es 0, entonces podremos conectar con servidor
    if ping_response == 0:
        try:
            #Se iniciliza el cliente ssh de paramiko
            client = paramiko.SSHClient()
            #Configuramos para pasar con credenciales propias
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #Ingresamos la contraseña
            input_password = getpass("Ingrese la contraseña: ")
            # Otra forma de evitar el error de host_know
            # client.load_system_host_keys()
            #Conectamos con el cliente
            client.connect(HOST, username=USER, password=input_password)
            #Ejecutamos el conmando y retorna la salida, entrada y error 
            stdin, stdout, stderr= client.exec_command("ls")
            #Se para un segundo el proceso
            time.sleep(1)
            #Se obtiene el resultado y se imprime
            result = stdout.read().decode()
            print(result)
            #Se cierra sesion
            client.close()
            
        #En caso de alguna falla, salta este except y presenta el problema    
        except paramiko.SSHException as ssh_e:
            print("Error al conectar: "+str(ssh_e))
    else:
        #Salta una exception si no hay conexion al servidor 
        raise Exception("conexión no establecida con el servidor") 