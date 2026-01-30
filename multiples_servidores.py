
# multi_client.py
import socket, json, time

DISC_PORT = 9999
TCP_TIMEOUT = 5

def discover(timeout=1.0):
    # Broadcast UDP: recibe respuestas "PROC_SRV <PORT>"
    found = []
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(timeout)
    s.sendto(b"DISCOVER_PROC_SRV", ("255.255.255.255", DISC_PORT))
    t0 = time.time()
    while time.time() - t0 < timeout:
        try:
            msg, (ip, _) = s.recvfrom(1024)
            parts = msg.decode().strip().split()
            if len(parts)==2 and parts[0]=="PROC_SRV":
                found.append((ip, int(parts[1])))
        except socket.timeout:
            break
    return list(dict.fromkeys(found))  # únicos

def send(ip, port, req):
    with socket.create_connection((ip, port), timeout=TCP_TIMEOUT) as c:
        c.sendall((json.dumps(req)+"\n").encode())
        return json.loads(c.makefile().readline())

if __name__ == "__main__":
    svcs = discover()
    if not svcs:
        print("No se encontraron servidores. ¿server.py está corriendo?"); exit(0)
    print("Servidores:", svcs)

    while True:
        print("\n1) Listar  2) Iniciar  3) Detener  4) Ver lanzados  0) Salir")
        op = input("Opción: ").strip()
        if op == "0": break
        req = None
        if op == "1": req = {"action":"list"}
        elif op == "2": req = {"action":"start","cmd": input("Comando: ")}
        elif op == "3": req = {"action":"kill","pid": int(input("PID: "))}
        elif op == "4": req = {"action":"list_launched"}
        else: print("Opción inválida"); continue

        for ip,port in svcs:
            try:
                r = send(ip, port, req)
                print(f"\n--- {ip}:{port} ---")
                if isinstance(r.get("data"), str):   # list() devuelve texto
                    print(r["data"], end="")
                else:
                    print(r)
            except Exception as e:
                print(f"\n--- {ip}:{port} --- error: {e}")
