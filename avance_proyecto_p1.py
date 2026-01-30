{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "51ef41e2",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid non-printable character U+00A0 (Temp/ipykernel_21568/719201690.py, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\sayuri\\AppData\\Local\\Temp/ipykernel_21568/719201690.py\"\u001b[1;36m, line \u001b[1;32m6\u001b[0m\n\u001b[1;33m    os.system(\"ps -eo pid,comm,pcpu,pmem | head\") #ps para enlistar primeras 10 lineas\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid non-printable character U+00A0\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import os # importar comandos del sistema operativo\n",
    "import time #pausar entre monitoreos\n",
    "# nota cambiar os.system por subprocess\n",
    "\n",
    "def listar():\n",
    "    os.system(\"ps -eo pid,comm,pcpu,pmem | head\") #ps para enlistar primeras 10 lineas\n",
    "def iniciar():\n",
    "    cmd = input(\"Comando a iniciar: \") #cambiar para capturar el pid\n",
    "    os.system(f\"{cmd} &\")\n",
    "def detener():\n",
    "    pid = input(\"PID a detener: \") # termina el proceso\n",
    "    os.system(f\"kill {pid}\")\n",
    "def monitorear(): #muestra primeras 5 lineas del sistema.\n",
    "    for i in range(5):\n",
    "        print(\"\\nCPU y Memoria:\")\n",
    "        os.system(\"top -b -n1 | head -5\")\n",
    "        time.sleep(1)\n",
    "while True:\n",
    "    print(\"\\n1) Listar procesos\")\n",
    "    print(\"2) Iniciar proceso\")\n",
    "    print(\"3) Detener proceso\")\n",
    "    print(\"4) Monitorear CPU/Memoria\")\n",
    "    print(\"0) Salir\")\n",
    "    op = input(\"Opción: \")\n",
    "    if op == \"1\": listar()\n",
    "    elif op == \"2\": iniciar()\n",
    "    elif op == \"3\": detener()\n",
    "    elif op == \"4\": monitorear()\n",
    "    elif op == \"0\": break\n",
    "    else: print(\"Opción no válida\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff760b69",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
