# CND-Emissor

Esse script tem como objetivo facilitar o controle de certidões negativas e jurídicas da Prefeitura de Santo André.

Seu uso consiste em dois simples caminhos, sendo o primeiro a busca por uma certidão avulsa, e o segundo a buscar por várias certidões.

A segunda opção do script é a que possui maior notoriedade em todo o seu uso, visto que grandes volumes de certidões precisam ser emitidos de maneira práticas e ágil.
Dessa maneira, caso deseje fazer o controle de uma vaga variedade de empresas é necessário criar um arquivo .TXT e listar nele todas as inscrições municipais que serão solicitadas
e após isso colocar o mesmo arquivo na mesma pasta do script.

Vide o seguinte exemplo:

>>> cat Inscrições-municipais.txt

#Inscricoes

123456
789101
112131
415161

Sendo assim, você terá uma lista com diversas inscrições municipais, e todas elas serão obtidas de maneira otimizada pelo script, cada qual nomeada mediante a sua identificação e
salva na mesma pasta do script. Caso haja alguma pendência em cima de alguma empresa, no final do código haverá uma notificação listando as empresas as que possuem tal pendência.

No mais, o script é bem agrádavel ao usuário e de bom uso para com o seu objetivo.

Sobre as bibliotecas externas utilizadas no projeto, são elas:

- Selenium (Responsável pela interação entre o python e a web)

- Requests (Responsável por efetuar o download do arquivo PDF)

O download dessas bibliotecas é facilmente obtido e compreendido em várias páginas da internet, não há segredo ou dificuldade na instalação.
