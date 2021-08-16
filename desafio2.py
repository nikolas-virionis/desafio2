import psutil
import time

def maquinas():
    print("\n\nOpções de visualização:\n\n\t 0 - todos\n \t1 - maquina 1\n \t2 - maquina 2\n \t3 - maquina 3\n")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 0:
        return [1, 2, 3]
    elif escolha == 1:
        return [1]
    elif escolha == 2:
        return [2]
    elif escolha == 3:
        return [3]
    else:
        print("insira um valor válido")

def metrics():
    while True:

        try:
            times = int(input("\nQuantas vezes deseja verificar as métricas de seu computador? "))
            interval = int(input("\nDe quantos em quantos segundos deseja medir essa métrica? "))
            break
        except:
            print(" Erro no numero inserido\n Tente novamente: \n")

    cpu1 = psutil.cpu_percent(interval = 1)
    disco1 = psutil.disk_usage('/').percent
    ram1 = psutil.virtual_memory().percent
    
    #print(type(cpu1), disco1, ram1)
    
    cpu2 = cpu1 * 1.1
    disco2 = disco1 * 0.95
    ram2 = ram1 * 1.15

    
    cpu3 = cpu1 * 1.15
    disco3 = disco2 * 3
    ram3 = ram1 * 1.1

    escolhas = maquinas()
    for i in range(times):
        if 1 in escolhas:
            if disco1 >= 90:
                print("Maquina 1 com excesso no uso de disco. \n\t\t\tMANUTENÇÃO IMEDIATA")
            print(f"\nMáquina 1:\n Uso de CPU: {cpu1:.2f}% \n Uso de Disco: {disco1:.2f}% \n Uso de Memória: {ram1:.2f}% \n\n")
        if 2 in escolhas:
            if disco2 >= 90:
                print("Maquina 2 com excesso no uso de disco. \n\t\t\tMANUTENÇÃO IMEDIATA")
            print(f"\nMáquina 2:\n Uso de CPU: {cpu2:.2f}% \n Uso de Disco: {disco2:.2f}% \n Uso de Memória: {ram2:.2f}% \n\n")
        if 3 in escolhas:
            if disco3 >= 90:
                print("Maquina 3 com excesso no uso de disco. \n\t\t\tMANUTENÇÃO IMEDIATA")
            print(f"\nMáquina 3:\n Uso de CPU: {cpu3:.2f}% \n Uso de Disco: {disco3:.2f}% \n Uso de Memória: {ram3:.2f}% \n\n")
        print("---------------------------------------------------------")
        time.sleep(interval)

metrics()
# Grupo 6 - SafeLog
# Amanda RA:02211001
# Felipe Cruz RA:01211037
# Joao Pedro RA: 02211036
# Lucas Menezes RA: 02211043
# Lucas Mesquita RA: 02211044
# Nikolas RA: 02211049

