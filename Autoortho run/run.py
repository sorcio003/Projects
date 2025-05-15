import os

os.system("SSL_CERT_DIR=/etc/ssl/certs ./autoortho_lin_0.7.1.bin")

for cartella, sottocartelle, files in os.walk(os.getcwd()):
    print(f"Ci troviamo nella cartella: '{cartella}'")
    print(f"Le sottocartelle presenti sono: '{sottocartelle}'")
    print(f"I files presenti sono: {files}")
    print()