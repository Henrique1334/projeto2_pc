import random
import datetime

def menu():
    nome_arq = "log.txt"
    while True:
        print('Monitor logPy')
        print("1 - gerar logs")
        print("2 - analisar logs")
        print("3- gerar e analisar logs")
        print("4- sair")
        opcao = input("escolha uma opcao:")
        if opcao == "1":
            try:
                qtd= int(input("quantidade de logs"))
                gerarArquivo(nome_arq,qtd)
            except:
                print("qtd incorreta")
        elif opcao == "2":
            analisarLog(nome_arq)
        elif opcao == "3":
            try:
                qtd= int(input("quantidade de logs"))
                gerarArquivo(nome_arq,qtd)
                analisarLog(nome_arq)
            except:
                print("qtd incorreta")
        elif opcao == "4":
            print("ate mais")
            break
        else:
            print("opcao errada")
            
def gerarArquivo(nome_arq,qtd):
    with open(nome_arq,qtd, "w", encoding="UTF-8") as arq:
        for i in range(qtd):
            arq.write(montarLog(1) + "\n")
        print('logs gerados')

def montarLog(i):
    data = gerarDataHora(i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo= gerarMetodo(i)
    status = gerarStatus(i)
    tempo= gerarTempo(i)
    agente = gerarAgente(i)
    return f'[({data}] {ip} - {metodo} -{status} - { recurso} - {tempo}ms - 500mb - HTTP/1.1- {agente} -/home"

def gerarDataHora(i):
    base = datetime.datetime(2026,3,30,22,8,0)
    data= datetime.timedelta(seconds=i * random.randint(5,20))
    return (base + data).strftime("%d/%m/%Y/%H/%S:")
    
def gerarIp(i):
    r= random.randint(1,6)
    
    if i >=20 and i <=30:
        return "200.0.111.345"
        
    if r== 1:
        return "192.168.5.8"
    elif r==2:
        return"192.168.5.8"
    elif r== 3:
        return"192.168.5.9"
    elif r ==4:
        return"192.168.5.8"
    elif r==5:
        return"192.168.25.8"
    else:
        return"192.168.65.68"
        

    
            
            
