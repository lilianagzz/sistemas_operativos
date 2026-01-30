import os # importar comandos del sistema operativo
import time #pausar entre monitoreos
# nota cambiar os.system por subprocess

def listar():
    os.system("ps -eo pid,comm,pcpu,pmem | head") #ps para enlistar primeras 10 lineas
def iniciar():
    cmd = input("Comando a iniciar: ") #cambiar para capturar el pid
    os.system(f"{cmd} &")
def detener():
    pid = input("PID a detener: ") # termina el proceso
    os.system(f"kill {pid}")
def monitorear(): #muestra primeras 5 lineas del sistema.
    for i in range(5):
        print("\nCPU y Memoria:")
        os.system("top -b -n1 | head -5")
        time.sleep(1)
while True:
    print("\n1) Listar procesos")
    print("2) Iniciar proceso")
    print("3) Detener proceso")
    print("4) Monitorear CPU/Memoria")
    print("0) Salir")
    op = input("Opción: ")
    if op == "1": listar()
    elif op == "2": iniciar()
    elif op == "3": detener()
    elif op == "4": monitorear()
    elif op == "0": break
    else: print("Opción no válida")