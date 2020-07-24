from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import os

def cls():
    os.system('cls')

def menu(): #Funcao para carregar o menu e suas opcoes
    print(""" ___________________________________________________________
             +   ____ ____     _____ __  __ ___ ____ ____   ___  ____    +
             |  / ___/ ___|   | ____|  \/  |_ _/ ___/ ___| / _ \|  _ \   |
             | | |   \___ \   |  _| | |\/| || |\___ \___ \| | | | |_) |  |
             | | |___ ___) |  | |___| |  | || | ___) ___) | |_| |  _ <   |
             |  \____|____/   |_____|_|  |_|___|____|____/ \___/|_| \_\  |
             |___________________________________________________________|
             |***********************************************************|
             | Esse programa tem como finalidade emitir as certidões     |
             |          municipais da Prefeitura de Santo André.         |
             |___________________________________________________________|
             |***********************************************************|
             |               Criado por: Kayque N Vieira                 |
             |                           V.1.0                           |
             |              https://controlsigma.com.br/                 |
             +___________________________________________________________+
             *************************************************************
             *************************************************************
              ___________________________________________________________
             +  Para utilizar o programa, favor escolher uma das opções  +
             |___________________________________________________________|
             |                    |                   |                  |
             |  Emitir pela lista |  Emitir pelo CMC  |   Informações    |
             |      Insira: L     |     Insira: C     |    Insira: I     |
             +____________________|___________________|__________________+ """)


    inp = (input("\n>>>Insira uma opção: ").upper().strip())
    pendencia = []

    if not inp in ["L","l","C","c","I","i"]:
        print("\nFavor inserir um valor válido.")
        time.sleep(3)
        menu()
        inp()
        
    
    elif inp == "C":   
        print("\nInsira a quantidade de certidões que você deseja solicitar.")
        lst = []
        num = int(input("\n>>>Quantidade: ")).strip()
        for x in range(0,num):
            cmc = str(input("\n>>>Por gentileza, inserir o CMC da empresa: ")).strip()
            print("*******************************************")
            lst.append(cmc)

        i = len(lst)
        insc = lst[0]
        print("\n>>>As certidões estão sendo emitidas, assim que finalizadas iremos notificar...")

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
            
            time.sleep(45) #Tempo médio para a aquisição do PDF ser liberada
    
            if driver.current_url == 'https://www.santoandre.sp.gov.br/PortalServico/Seguranca/frmLogin.aspx':
                print("\nA certidão {} está com pendência.".format(insc))
                print("*******************************{}".format("*"*len(insc)))
                pendencia.append(insc)    
            else:
                   #Requests obtem o link do Selenium e utiliza-o para baixar o arquivo PDF
                    pdf_url = (driver.find_element_by_tag_name('iframe').get_attribute("src"))
                    url = pdf_url               
                    ext = '.pdf' #Renomea-se o arquivo para .pdf
                    r = requests.get(url)
                    with open(str(insc)+ext, 'wb') as f:
                     f.write(r.content)
                    print("\nA certidão sobre a inscrição {} foi salva com sucesso !".format(insc))
                    print("*****************************************************{}".format("*"*len(insc)))                  

            i = i-1
            insc = lst[0+i]
        
        if i == 0:
            print("As certidões foram emitidas com sucesso.")
            if len(pendencia) > 0:
                print("A quantidade de inscrições com pendências é de: {}.\nInscrições com pendência: {}".format(len(pendencia),pendencia))

    elif inp == "I":
        cls()
        print("""
         ________________________________________________________________
        +      ____ ____     _____ __  __ ___ ____ ____   ___  ____      +
        |     / ___/ ___|   | ____|  \/  |_ _/ ___/ ___| / _ \|  _ \     |
        |    | |   \___ \   |  _| | |\/| || |\___ \___ \| | | | |_) |    |
        |    | |___ ___) |  | |___| |  | || | ___) ___) | |_| |  _ <     |
        |     \____|____/   |_____|_|  |_|___|____|____/ \___/|_| \_\    |
        |________________________________________________________________|
        |****************************************************************|
        | Os arquivos emitidos por esse programa são obtidos diretamente |
        | pelo sistema oficial de emissão de certidões da PMSA, ou seja, |
        | qualquer erro visualizado pelo programa deve ser analisado em  |
        | grande parte por funcão do respectivo site.Alguns erros comuns |
        | que podem por algum motivo ocorrer são:                        |
        |                                                                |
        | I.  Conexão com a internet interrompiada;                      |
        | II. Site da Prefeitura de Santo André está indisponível;       |
        | III.Inicialização do programa com algum erro.                  |
        |                                                                |
        | Para todas as situações acima, o problema pode ser facilmente  |
        | resolvido, presumo que o usuário tenha um conhecimento básico. |
        | Para outras dúvidas relacionadas ao programa em geral basta    |
        | enviar um e-mail para o seguinte contato:                      |
        |                                                                |
        |                 >>>Kayquenv@Outlook.com<<<                     |
        |________________________________________________________________|
        |****************************************************************|
        |       Página inicial          |        Sair do programa        |
        |         Inserir: H            |            Inserir: S          |
        +________________________________________________________________+ """)

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
        num = (input("\n>>>Grupo: ").upper())

        if num == "M":
            grupo = lista[1:14]
        elif num == "1":
            grupo = lista[15:25]
        elif num == "2":
            grupo = lista[26:36]
        elif num == "3":
            grupo = lista[37:47]
        elif num == "4":
            grupo = lista[48:59]
        elif num == "5":
            grupo = lista[60:76]
        elif num == "6":
            grupo = lista[77:90]
        elif num == "7":
            grupo = lista[91:103]
        elif num == "8":
            grupo = lista[104:113]
        elif num == "9":
            grupo = lista[114:125]
        elif num == "10":
            grupo = lista[126:134]
        elif num == "11":
            grupo = lista[135:147]
        elif num == "12":
            grupo = lista[148:158]
        elif num == "13":
            grupo = lista[159:169]
        elif num == "14":
            grupo = lista[170:179]
        elif num == "15":
            grupo = lista[180:184]
        i = len(grupo)
        vargrupo = grupo[0]

        while i >= 0:
    
            chrome_options = Options()
            #chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('https://www.santoandre.sp.gov.br/portalservico/Certidoes/PosNegTribMobiliario.aspx')

#Selenium submete a inscricao na box xpath CMC
            xpathbox = '//*[@id="ContentPlaceHolder1_txtCMC"]'
            box = driver.find_element_by_xpath(xpathbox)
            box.send_keys(vargrupo)
            box.submit()

#Selenium submete um clique para prosseguir com a emissao
            xpathbtn = '//*[@id="ContentPlaceHolder1_btnVisualizar"]'
            btn = driver.find_element_by_xpath(xpathbtn)
            btn.click()

#Requests obtem o link do Selenium e utiliza-o para baixar o arquivo PDF
            
            time.sleep(45) #Tempo médio para a aquisição do PDF ser liberada
          
            pdf_url = driver.find_element_by_tag_name('iframe').get_attribute("src")
            print(pdf_url) #Link aonde o PDF esta hospedado
            url = pdf_url

            ext = '.pdf' #Renomea-se o arquivo para .pdf
            r = requests.get(url)
            with open(str(vargrupo)+ext, 'wb') as f:
             f.write(r.content)

#Loop para prosseguir com as emissoes que o usuario solicitou
            print("\nA certidão sobre a inscrição {} foi salva com sucesso !".format(vargrupo))
            print("*****************************************************{}".format("*"*len(vargrupo)))
            
            i = i-1
            vargrupo = grupo[0+i]

            if i == 0:
                print("As certidões fora emitidas com sucesso e salvas no diretório do programa.")
                              
menu()
