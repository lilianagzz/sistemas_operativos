# server.py
import socket, threading, json, subprocess, shlex

LAUNCHED = set()                     # PIDs iniciados por este servidor
HOST, PORT = "0.0.0.0", 5000         # escucha en todas las interfaces

def ps_snapshot():
    out = subprocess.check_output(["ps","-eo","pid,comm,pcpu,pmem","--no-header"])
    return out.decode(errors="ignore")

def handle(conn, addr):
    f = conn.makefile("rwb")
    while True:
        line = f.readline()
        if not line: break
        try:
            req = json.loads(line)
            act = req.get("action")
            if act == "list":
                resp = {"ok": True, "data": ps_snapshot()}
            elif act == "start":
                cmd = shlex.split(req.get("cmd",""))
                p = subprocess.Popen(cmd)      # seguro (sin shell)
                LAUNCHED.add(p.pid)
                resp = {"ok": True, "pid": p.pid}
            elif act == "kill":
                pid = str(req.get("pid"))
                if int(pid) in LAUNCHED:
                    subprocess.run(["kill", pid], check=False)
                    LAUNCHED.discard(int(pid))
                    resp = {"ok": True}
                else:
                    resp = {"ok": False, "error": "PID no fue iniciado por este servidor"}
            elif act == "list_launched":
                resp = {"ok": True, "data": sorted(LAUNCHED)}
            else:
                resp = {"ok": False, "error": "acción desconocida"}
        except Exception as e:
            resp = {"ok": False, "error": str(e)}
        f.write((json.dumps(resp)+"\n").encode()); f.flush()
    conn.close()

def tcp_server():
    with socket.create_server((HOST, PORT), reuse_port=True) as s:
        print(f"Servidor procesos en {HOST}:{PORT}")
        while True:
            c, a = s.accept()
            threading.Thread(target=handle, args=(c,a), daemon=True).start()

# --- Descubrimiento (para Tarea 3): responder por UDP ---
def udp_discovery():
    # Responde a "DISCOVER_PROC_SRV" en el puerto 9999 con: "PROC_SRV <PORT>"
    import time
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 9999))
    while True:
        msg, peer = sock.recvfrom(1024)
        if msg.strip() == b"DISCOVER_PROC_SRV":
            sock.sendto(f"PROC_SRV {PORT}".encode(), peer)
        time.sleep(0.01)

if __name__ == "__main__":
    threading.Thread(target=udp_discovery, daemon=True).start()
    tcp_server()