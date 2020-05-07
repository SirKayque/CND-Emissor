from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
      
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
print("|              https://controlsigma.com.br/                 |")
print("+___________________________________________________________+")
print("*************************************************************")
print("*************************************************************")


print(" __________________________________________________________")
print("|  Para utilizar o programa, favor escolher uma das opções |")
print("|_________________________________________________________ |")
print("|                    |                  |                  |")
print("|  Emitir pela lista |  Emitir pelo CMC |    Informações   |")
print("|      Insira: L     |      Insira: C   |     Insira: I    |")
print("|_______________________________________|__________________|")


##Se C

inp = (input("\nInsira uma opção: ").upper())

if inp == "C":   
    print("\nQuantas inscrições você pretende emitir ?")
    lst = []
    num = int(input("\nQuantidade: "))
    for i in range(0,num):
        cmc = int(input("\nFavor, inserir o CMC da empresa: "))
        lst.append(cmc)

i = len(lst)
print(i)

while i > 0:
        insc = lst[0]

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.santoandre.sp.gov.br/portalservico/Certidoes/PosNegTribMobiliario.aspx')

#Input CMC
        xpathbox = '//*[@id="ContentPlaceHolder1_txtCMC"]'
        box = driver.find_element_by_xpath(xpathbox)
        box.send_keys(insc)
        box.submit()

#Submit CMC
        xpathbtn = '//*[@id="ContentPlaceHolder1_btnVisualizar"]'
        btn = driver.find_element_by_xpath(xpathbtn)
        btn.click()

#Downlad PDF
        time.sleep(35) #Tempo médio para a aquisição do PDF ser liberada

        pdf_url = driver.find_element_by_tag_name('iframe').get_attribute("src")
        print(pdf_url)
        url = pdf_url

        ext = '.pdf'
        r = requests.get(url)
        with open(str(insc)+ext, 'wb') as f:
         f.write(r.content)

        print("A certidão sobre a inscrição {} salvo com sucessos !".format(cmc))
        
insc = (lst[0+1])
i = i-1
