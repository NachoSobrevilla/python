# Ejemplo de URL: https://www.ncbi.nlm.nih.gov/nuccore/NM_001273567.1?report=fasta
# https://www.ncbi.nlm.nih.gov/nuccore/ <NCBI Reference Sequence> ?report=fasta

# https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=fasta&id=*<ID de la secuencia>*&conwithfeat=on&hide-cdd=on&ncbi_phid=null

# import wget

# #Se define la URL del archivo a descargar
# remote_url = 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=fasta&id=DQ914860.1&conwithfeat=on&hide-cdd=on&ncbi_phid=null'

# #Se define el nombre del archivo a descargar
# local_file = 'DQ914860.1.fasta'

# #Se carga el archivo y se guarda el archivo de forma local 
# try:
#     wget.download(remote_url, local_file)
# except Exception as e:
#     print("No se pudo descargar el archivo | Could not download file {}".format(local_file))
#     print(e)

import requests


# remote_url = 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=fasta&id=DQ914860.1&conwithfeat=on&hide-cdd=on&ncbi_phid=null'
remote_url = 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=fasta&id=ASBCS&conwithfeat=on&hide-cdd=on&ncbi_phid=null'
sequence = requests.get(remote_url)
print(sequence.raise_for_status())
print(sequence.content)
# try:
#     sequence = requests.get(remote_url)
# except (requests.ConnectionError, requests.Timeout):
#     print("Error: Don't found the sequence(s), check your internet conexion")
#     print(sequence.content)