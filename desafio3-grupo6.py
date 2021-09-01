import psutil
import time


def componente():
    while True:
        print("\n\nOpções de visualização:\n\n\t0 - todos\n \t1 - cpu\n \t2 - ram\n \t3 - disco\n \t4 - internet\n")
        escolha = int(input("Escolha uma opção: "))
        if escolha == 0:
            return [1, 2, 3, 4]
        if escolha in range(1, 5):
            return [escolha]
        print("insira um valor válido")


def metrics():
    componentes = componente()
    visualizacao(componentes)


def dados(escolhas):
    maquina = []
    componente1 = {
        "nome": "CPU",
        "nome1": "Porcentagem de CPU",
        "nome2": "Frequencia de CPU",
        "dado1": f"{psutil.cpu_percent(interval=1)}%",
        "dado2": f"{psutil.cpu_freq().current}MHz"
    }
    componente2 = {
        "nome": "Memória Principal",
        "nome1": "Quantidade de RAM livre",
        "nome2": "Percentual de uso de RAM",
        # 1048576 byte -> 1 Megabyte
        "dado1": f"{round((psutil.virtual_memory().free / 1048576), 2)}MB",
        "dado2": f"{psutil.virtual_memory().percent}%"
    }
    componente3 = {
        "nome": "Memória em disco",
        "nome1": "Quantidade de memoria em disco livre",
        "nome2": "Percentual de memoria de disco em uso",
        # 1073741824 byte -> 1 Gigabyte
        "dado1": f"{round((psutil.disk_usage('/').free / 1073741824), 2)}GB",
        "dado2": f"{psutil.disk_usage('/').percent}%"
    }
    componente4 = {
        "nome": "Internet",
        "nome1": "Bytes recebidos",
        "nome2": "Bytes enviados",
        # 1048576 byte -> 1 Megabyte
        "dado1": f"{round((psutil.net_io_counters().bytes_recv / 1048576), 2)}MB",
        # 1048576 byte -> 1 Megabyte
        "dado2": f"{round((psutil.net_io_counters().bytes_sent / 1048576), 2)}MB"
    }
    for i in escolhas:
        maquina.append(eval(f"componente{i}"))
    return maquina


def visualizacao(escolhas):
    while True:
        maquina = dados(escolhas)
        for componente in maquina:
            print(
                f'\n{componente["nome"]}:\n\t{componente["nome1"]}: {componente["dado1"]}\n\t{componente["nome2"]}: {componente["dado2"]}')
        if(1 in escolhas and psutil.cpu_freq().current*1.21 / psutil.cpu_freq().max > 1.2):
            print(
                "\n\n\tCPU rodando em overclock com frequência mais de 20% maior que o máximo, \n\t\t\t\t\tPERIGO")
        print("-"*70)
        time.sleep(2)


metrics()


# Grupo 6 - SafeLog
# Amanda         RA: 02211001
# Felipe Cruz    RA: 01211037
# Joao Pedro     RA: 02211036
# Lucas Menezes  RA: 02211043
# Lucas Mesquita RA: 02211044
# Nikolas        RA: 02211049
