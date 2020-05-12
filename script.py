from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import os

def cls():
    os.system('cls')

def menu(): #Funcao para carregar o menu e suas opcoes
    print(" ___________________________________________________________")
    print("+   ____ ____     _____ __  __ ___ ____ ____   ___  ____    +")
    print("|  / ___/ ___|   | ____|  \/  |_ _/ ___/ ___| / _ \|  _ \   |")
    print("| | |   \___ \   |  _| | |\/| || |\___ \___ \| | | | |_) |  |")
    print("| | |___ ___) |  | |___| |  | || | ___) ___) | |_| |  _ <   |")
    print("|  \____|____/   |_____|_|  |_|___|____|____/ \___/|_| \_\  |")
    print("|___________________________________________________________|")
    print("|***********************************************************|")
    print("| Esse programa tem como finalidade emitir as certidões     |")
    print("|          municipais da Prefeitura de Santo André.         |")
    print("|___________________________________________________________|")
    print("|***********************************************************|")
    print("|               Criado por: Kayque N Vieira                 |")
    print("|                           V.1.0                           |")
    print("|              https://controlsigma.com.br/                 |")
    print("+___________________________________________________________+")
    print("*************************************************************")
    print("*************************************************************")

    print(" ___________________________________________________________")
    print("+  Para utilizar o programa, favor escolher uma das opções  +")
    print("|___________________________________________________________|")
    print("|                    |                   |                  |")
    print("|  Emitir pela lista |  Emitir pelo CMC  |   Informações    |")
    print("|      Insira: L     |     Insira: C     |    Insira: I     |")
    print("+____________________|___________________|__________________+")


    ##Se a opcao selecionada for C
    inp = (input("\n>>>Insira uma opção: ").upper())

    if inp == "C":   
        print("\nInsira a quantidade de certidões que você deseja solicitar.")
        lst = []
        num = int(input("\n>>>Quantidade: "))
        for x in range(0,num):
            cmc = str(input("\n>>>Por gentileza, inserir o CMC da empresa: "))
            print("*******************************************")
            lst.append(cmc)

        i = len(lst)
        insc = lst[0]
        print("\n>>>As certidões estão sendo emitir, assim que finalizadas iremos notificar")

        while i > 0:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('https://www.santoandre.sp.gov.br/portalservico/Certidoes/PosNegTribMobiliario.aspx')

#Selenium submete a inscricao na box xpath CMC
            xpathbox = '//*[@id="ContentPlaceHolder1_txtCMC"]'
            box = driver.find_element_by_xpath(xpathbox)
            box.send_keys(insc)
            box.submit()

#Selenium submete um clique para prosseguir com a emissao
            xpathbtn = '//*[@id="ContentPlaceHolder1_btnVisualizar"]'
            btn = driver.find_element_by_xpath(xpathbtn)
            btn.click()

#Requests obtem o link do Selenium e utiliza-o para baixar o arquivo PDF
            
            time.sleep(40) #Tempo médio para a aquisição do PDF ser liberada

            pdf_url = driver.find_element_by_tag_name('iframe').get_attribute("src")
            print(pdf_url) #Link aonde o PDF esta hospedado
            url = pdf_url

            ext = '.pdf' #Renomea-se o arquivo para .pdf
            r = requests.get(url)
            with open(str(insc)+ext, 'wb') as f:
             f.write(r.content)
             
#Loop para prosseguir com as emissoes que o usuario solicitou
            print("\nA certidão sobre a inscrição {} foi salva com sucesso !".format(insc))
            print("*****************************************************{}".format("*"*len(insc)))
            i = i-1
            insc = lst[0+i]

    elif inp == "I":
        cls()
        print(" ________________________________________________________________")
        print("+      ____ ____     _____ __  __ ___ ____ ____   ___  ____      +")
        print("|     / ___/ ___|   | ____|  \/  |_ _/ ___/ ___| / _ \|  _ \     |")
        print("|    | |   \___ \   |  _| | |\/| || |\___ \___ \| | | | |_) |    |")
        print("|    | |___ ___) |  | |___| |  | || | ___) ___) | |_| |  _ <     |")
        print("|     \____|____/   |_____|_|  |_|___|____|____/ \___/|_| \_\    |")
        print("|________________________________________________________________|")
        print("|****************************************************************|")
        print("| Os arquivos emitidos por esse programa são obtidos diretamente |")
        print("| pelo sistema oficial de emissão de certidões da PMSA, ou seja, |")
        print("| qualquer erro visualizado pelo programa deve ser analisado em  |")
        print("| grande parte por funcão do respectivo site.Alguns erros comuns |")
        print("| que podem por algum motivo ocorrer são:                        |")
        print("|                                                                |")
        print("| I.  Conexão com a internet interrompiada;                      |")
        print("| II. Site da Prefeitura de Santo André está indisponível;       |")
        print("| III.Inicialização do programa com algum erro.                  |")
        print("|                                                                |")
        print("| Para todas as situações acima, o problema pode ser facilmente  |")
        print("| resolvido, presumo que o usuário tenha um conhecimento básico. |")
        print("| Para outras dúvidas relacionadas ao programa em geral basta    |")
        print("| enviar um e-mail para o seguinte contato:                      |")
        print("|                                                                |")
        print("|                 >>>Kayquenv@Outlook.com<<<                     |")
        print("|________________________________________________________________|")
        print("|****************************************************************|")
        print("|       Página inicial          |        Sair do programa        |")
        print("|         Inserir: H            |            Inserir: S          |")
        print("+________________________________________________________________+")


        opc = (str(input("\n>>>Insira uma opção: ").upper()))
        if opc == "H":
                cls()
                menu()
        elif opc == "S":
                exit()

    elif inp == "L":
        lista = open("lista.txt").read().splitlines()
        print("\nInsira o grupo que você desejea emitir.")
        print("Exemplo, insira 1 para o Grupo 01, ou 15 para o Grupo 15.")
        num = int(input("\n>>>Grupo: "))

        if num == "M":
            lista = lista[1:14]
        elif num == 1:
            lista = lista[16:25]
        elif num == 2:
            lista = lista[27:36]
        elif num == 3:
            lista = lista[38:47]
        elif num == 4:
            lista = lista[49:59]
        elif num == 5:
            lista = lista[61:76]
        elif num == 6:
            lista = lista[78:90]
        elif num == 7:
            lista = lista[92:103]
        elif num == 8:
            lista = lista[105:113]
        elif num == 9:
            lista = lista[115:125]
        elif num == 10:
            lista = lista[127:134]
        elif num == 11:
            lista = lista[136:147]
        elif num == 12:
            lista = lista[149:158]
        elif num == 13:
            lista = lista[160:169]
        elif num == 14:
            lista = lista[171:179]
        elif num == 15:
            lista = lista[181:184]

                
menu()
