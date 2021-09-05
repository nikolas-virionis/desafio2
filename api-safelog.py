import psutil
import time
from datetime import datetime

def machine(id):
    cpu = psutil.cpu_percent(interval=0.5) + 2
    mem = psutil.virtual_memory().percent
    dsk = psutil.disk_usage('/').percent
    now = datetime.now()
    datahora = now.strftime("%d/%m/%Y %H:%M:%S")

    return [id, cpu, mem, dsk, datahora]

def mac2simulation(array):
    return [array[0], array[1] * 1.1, array[2] * 1.1, array[3] * 1.1, array[4]]

def mac3simulation(array):
    return [array[0], array[1] * 0.9, array[2] * 0.9, array[3] * 0.9, array[4]]

def show(mac):
    print('-' * 15, f'maquina {mac[0]}', '-' * 15)
    print(f'cpu: {mac[1]:.2f}% de uso')
    print(f'memoria: {mac[2]:.2f}% de uso')
    print(f'disco: {mac[3]:.2f}% de uso')
    print(f'data e hora: {mac[4]}')

while True:
    machine1 = machine(1) 
    machine2 = mac2simulation(machine(2))
    machine3 = mac3simulation(machine(3))

    show(machine1)
    show(machine2)
    show(machine3)
    print("-" * 41)
    print("\n\n")
    time.sleep(10)