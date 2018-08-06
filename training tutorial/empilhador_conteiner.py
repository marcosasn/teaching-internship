#coding: utf-8
#Marcos Nascimento, 2018

EMPILHAR = "Empilhar"
DESEMPILHAR = "Desempilhar"
FIM_EXPEDIENTE = "Fim de expediente"
ponteiro_pilha = 0

capacidade = int(raw_input())
if capacidade > 0:
	while True:
		acao = raw_input()
		if acao == FIM_EXPEDIENTE:
			print "Navio está com {} conteiner(s).".format(ponteiro_pilha)
			break
		else:
			if acao == EMPILHAR:
				ponteiro_pilha += 1
				if ponteiro_pilha == capacidade:
					print "Navio está com carga completa."
					break
			if acao == DESEMPILHAR:
				if ponteiro_pilha == 0:
					print "Não há nenhum container no navio."
					break
				else:
					ponteiro_pilha -= 1 
