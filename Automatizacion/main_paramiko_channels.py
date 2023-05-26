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
            client.load_system_host_keys()
            #Conectamos con el cliente
            client.connect(HOST, username=USER, password=input_password)
            #Conectamos con el cliente 679603
            sftp_client = client.open_sftp()
            #put para montar los parametros (archivo y ruta de llegada) y 
            sftp_client.put('urls.txt','/Documents/folder1/urls.txt')
            
            #get es para traer un archivo ("ruta del archivo", llegada del archivo)
            sftp_client.get('/home/sobr3s/Documents/folder1/prueba.txt', 'prueba.txt')
            
            #se crea una sesión segura
            session = client.get_transport().open_session()
            #verifica si esta activa
            if session.active:
                #ejecuta el comando ls -l o cd
                session.exec_command('cd Documents/folder1 && ls -l')
                #vemos el resultado de la consola mediante recv, pasandole el numero de bits
                #y despues se descodifica
                result = session.recv(2048).decode()
                #Se imprime el resultado
                print(result)
            
            sftp_client.close()
            #Cerramos sesion
            client.close()
            
            
            
        #En caso de alguna falla, salta este except y presenta el problema    
        except paramiko.SSHException as ssh_e:
            print("Error al conectar: "+str(ssh_e))
    else:
        #Salta una exception si no hay conexion al servidor 
        raise Exception("conexión no establecida con el servidor") 