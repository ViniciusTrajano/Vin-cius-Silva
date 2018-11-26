import requests

r = requests.get('https://sites.google.com/site/el7hon/ensino/lac')
p = open('lac_doc.txt','w')
p.writelines(r.text)
p = open('lac_doc.txt','r')

while True:
    entrada = input('Programação para disciplina de Lógica Aplicada à Computação:\nO que deseja acessar: \nI - Identificação da disciplina.\nP - Prova. \nT - Trabalhos.\nEntrada: ')

    if entrada.lower() == "i":
        for line in p.readlines():
            if "<strong>Descrição:</strong>" in line :
                start = line.index("<strong>Descrição:</strong>") + 28
                end = line.index("</small>")
                print(line[start:end])
                break

    elif entrada.lower() == "p":
        for line in p.readlines():
            if '<strong>Prova' in line:
                start = line.index('<strong>Prova') + 8
                end = line.index('2018</strong>') +4
                print(line[start:end])
                break
    elif entrada.lower() == "t":
        for line in p.readlines():
            if '<li id="h.p_' in line:
                start = line.index('<li id="h.p_') + 46
                end = line.index(')</li>') + 1
                print(line[start:end])
                break
    else:
        print("\n------------------------------\nENTRADA INVALIDA!\n------------------------------")
    
