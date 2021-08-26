import psutil
import time


def maquinas():
    while True:
        print("\n\nOpções de visualização:\n\n\t0 - todos\n \t1 - maquina 1\n \t2 - maquina 2\n \t3 - maquina 3\n \t4 - maquinas 1 e 2\n \t5 - maquinas 1 e 3\n \t6 - maquinas 2 e 3\n")
        escolha = int(input("Escolha uma opção: "))
        if escolha == 0:
            return [1, 2, 3]
        if escolha in range(1, 4):
            return [escolha]
        if escolha == 4:
            return [1, 2]
        if escolha == 5:
            return [1, 3]
        if escolha == 6:
            return [2, 3]
        print("insira um valor válido")


def metrics():
    while True:
        try:
            times = int(
                input("\nQuantas vezes deseja verificar as métricas de seu computador? "))
            interval = int(
                input("\nDe quantos em quantos segundos deseja medir essa métrica? "))
            escolhas = maquinas()
            visualizacao(escolhas, times, interval)
            break
        except:
            print(" Erro no numero inserido\n Tente novamente: \n\n")


def dados(escolhas):
    maquinas = []
    maquina1 = {
        "maquina": 1,
        "cpu": psutil.cpu_percent(interval=1),
        "disco": psutil.disk_usage('/').percent,
        "ram": psutil.virtual_memory().percent
    }
    maquina2 = {
        "maquina": 2,
        "cpu": maquina1["cpu"] * 1.1,
        "disco": maquina1["disco"] * 0.95,
        "ram": maquina1["ram"] * 1.15
    }
    maquina3 = {
        "maquina": 3,
        "cpu": maquina1["cpu"] * 1.15,
        "disco": maquina2["disco"] * 3,
        "ram": maquina1["ram"] * 1.1
    }
    for i in escolhas:
        maquinas.append(
            eval(f"maquina{i}"))
    return maquinas


def visualizacao(escolhas, times, interval):
    for i in range(times):
        maquinas = dados(escolhas)
        for maquina in maquinas:
            for key, value in maquina.items():
                if value >= 90:
                    print(
                        f"Máquina {maquina['maquina']} com excesso no uso de {key}. \n\t\t\tMANUTENÇÃO IMEDIATA")
            print(
                f'\nMáquina {maquina["maquina"]}:\n Uso de CPU: {maquina["cpu"]:.2f}% \n Uso de Disco: {maquina["disco"]:.2f}% \n Uso de Memória: {maquina["ram"]:.2f}% \n\n')
        print("----------------------------------------------------------------------")
        time.sleep(interval)


while True:
    metrics()
    print("\n\n0 - sair \n1 - repetir medições")
    repeat = int(input("Escolha uma opção: "))
    if not repeat:
        break


# Grupo 6 - SafeLog
# Amanda         RA: 02211001
# Felipe Cruz    RA: 01211037
# Joao Pedro     RA: 02211036
# Lucas Menezes  RA: 02211043
# Lucas Mesquita RA: 02211044
# Nikolas        RA: 02211049
