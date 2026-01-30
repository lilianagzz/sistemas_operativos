
# client.py
import socket, json

HOST = input("IP del servidor (ej. 127.0.0.1): ").strip() or "127.0.0.1"
PORT = int(input("Puerto (5000 por defecto): ").strip() or 5000)

def send(req):
    with socket.create_connection((HOST, PORT), timeout=5) as c:
        c.sendall((json.dumps(req)+"\n").encode())
        data = c.makefile().readline()
        return json.loads(data)

while True:
    print("\n1) Listar procesos  2) Iniciar  3) Detener (solo lanzados)  4) Ver lanzados  0) Salir")
    op = input("Opción: ").strip()
    if op == "1":
        r = send({"action":"list"}); print(r.get("data",""), end="")
    elif op == "2":
        cmd = input("Comando (ej: sleep 100): ")
        r = send({"action":"start","cmd":cmd}); print(r)
    elif op == "3":
        pid = int(input("PID a detener: "))
        r = send({"action":"kill","pid":pid}); print(r)
    elif op == "4":
        r = send({"action":"list_launched"}); print("Lanzados:", r.get("data"))
    elif op == "0":
        break
