# coding: utf-8 

# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# --------------- Rotina de Sorteio de Brindes do TcheLinux --------------- #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #

import random
import math
import os

# Nome do pessoal que vai participar do sorteio
galera = [
			'Fulaninho',
			'Ciclaninho',
			'Pedrinho',
			# Coloque seu nome aqui! :)
		 ]

# ------------------------------------------------------------------------- #
# ---------- Início da Rotina de Sorteio de Brindes do TcheLinux ---------- #
# ------------------------------------------------------------------------- #

# Limpa a tela
os.system('clear')

print "Seja bem vindo ao sorteio de brindes do TcheLinux"

# Verifica nomes duplicados
if (len(galera) != len(set(galera))):
	print("\n-> ERRO! Algum(a) safadinho(a) se cadastrou duas vezes!\n")
	exit()

print "Uma vez sorteado, seu nome não será mostrado novamente.\n"
print "Existem "+str(len(galera))+" pessoas na lista do sorteio! Bora lá?\n"

while galera:
	# Prompt para sorteio
	sortearMais = raw_input("Sortear mais um [s/n]? ")
	
	if sortearMais == "s":
		# Nome do sorteado
		sorteado = random.choice(galera)
		print("\n-> E a pessoa sortuda é: "+sorteado+"\n")
		
		# Tira da lista
		galera.remove(sorteado)
		
	else:
		exit()
		
# Se ao sair do loop a lista estiver vazia, avisa que não existe mais o que sortear
print("Todas as pessoas já foram sorteadas.")