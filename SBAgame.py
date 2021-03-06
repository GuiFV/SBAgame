# -*- coding: utf-8 -*-

import os, sys, time, random

lg = ""
home = ""
speed = 50

colors = {             
    'RED': '\033[91m',     
    'GREEN': '\033[92m',   
    'END': '\033[0m',      
}

def prints(words,*args,**kwargs):
    for word in words:
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(random.random()*8.0/speed) #0.1 / 8.0
    print ('')

while lg != "en" or "pt":
	lg = input("English, type 'en' / Português, digite 'pt':")
	if lg == "en" or lg == "pt":
		break
	print ("\nPlease enter a valid option / Insira uma opção válida\n")
	continue

if lg == "en":
	welcome_message = "Welcome to SBA (System Based on Abundance)"
	welcome_2 = "Develop a better world... by improving yourself and your own environment"

else:
	welcome_message = "Bem vind@ ao SBA (Sistema Baseado em Abundância)"
	welcome_2 = "Crie um mundo melhor... aprimorando a você mesmo e ao seu ambiente"

print ("\n")
prints(welcome_message+"\n")
prints(welcome_2+"\n")

if lg == "en":
	name = input("Your name:")
	while home != 1 or 2 or 3:
		home = int(input("Where do you live? House = '1', Apartment = '2', Street = '3':"))
		if home == 1 or home == 2 or home == 3:
			break
		print ("\nPlease enter a valid option\n")
		continue
	home_size = float(input("How big is your home (in square meters):"))
	income = float(input("What is your monthly revenue? (type from '0.00' to '999,999,999.99'):"))
	designated = float(input("And from that income, how much can you invest in improvements to your home? (type from '0.00' to '999,999,999.99'):"))
	if home == 1:
		home = 'House'
	elif home == 2:
		home = 'Apartment'
	elif home == 3:
		home = 'Street'

else:
	name = input("Seu nome:")
	while home != 1 or 2 or 3:
		home = int(input("Onde você more? Casa = '1', Apartamento = '2', Rua = '3':"))
		if home == 1 or home == 2 or home == 3:
			break
		print ("\nInsira uma opção válida\n")
		continue
	home_size = float(input("Quão grande é seu lar (em metros quadrados):"))
	income = float(input("Qual sua receita mensal? (digite de '0.00' a '999,999,999.99'):"))
	designated = float(input("E dessa receita, quanto você pode investir em melhoras para seu lar? ((digite de '0.00' a '999,999,999.99'):"))
	if home == 1:
		home = 'Casa'
	elif home == 2:
		home = 'Apartamento'
	elif home == 3:
		home = 'Rua'

if lg == "en":
	prints("Plotting data. Please wait...")
	prints("Hello, {}.\n\nWe will be helping you in your {} with {} square meters.\nPlease choose the option below wisely so your designated {} investiment does not extrapolate you {} income.".format(name,home,home_size,designated,income))
else:
	prints("Plotando dados. Por favor aguarde...")
	prints("Olá, {}.\n\nNós iremos te ajudar com sua/seu {} que possui {} metros quadradoss.\nPor favor escolha as opções abaixo com cuidado para que sua renda de investimento de {} nao extrapole sua receita de {}.".format(name,home,home_size,designated,income))


user = [
[name,home,home_size,designated,income]
]

water_solutions = [
['1','Baixo','Captação de água de chuva','Borda do telhado','Garrafas PET, canos e reservatório','Menos de 1 mês'],
['2','Médio','Aparelho de condensação','2m²','Compra do aparelho','Menos de 1 mês'],
['99','Alto','Aparelho de condensação','2m²','Compra do aparelho','Menos de 1 mês'],

]


food_solutions = [

]

energy_solutions = [

]

automation_solutions = [

]


prints("O que deseja fazer agora?\n")

print ("1 - Quero produzir minha própria água\n2 - Quero produzir minha própria comida\n3 - Quero produzir minha própria enegia elétrica\n4 - Quero automatizar processos\n5 - Ver/Editar meus dados\n6 - Ver/Editar minhas soluções\n7 - Executar solução")

phase1_selector = int(input('Opção:'))

phase1_title = ("{GREEN} : ID  : Custo  : Solução                    : Espaço                 : Recursos necessários                           : Tempo necessário : {END}".format(**colors))

print (phase1_title)


if phase1_selector == 1:
	for sol in water_solutions:
		print (" :",sol[0]," "*(2-len(sol[0])),":",
					sol[1]," "*(5-len(sol[1])),":",
					sol[2]," "*(25-len(sol[2])),":",
					sol[3]," "*(21-len(sol[3])),":",
					sol[4]," "*(45-len(sol[4])),":",
					sol[5]," "*(15-len(sol[5])),": ")
		
else:
	print ('bugando')



sol_selector = input("Selecione o ID da solução:")




































