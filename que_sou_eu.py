import socket
import os

print("-" * 30)
print("ONDE ESTOU RODANDO?")
print("-" * 30)
print(f"Nome da máquina: {socket.gethostname()}")
print(f"Sistema operacional: {os.uname().sysname} {os.uname().release}")
print(f"Usuario logado: {os.getlogin()}")
print("-" * 30)