# coding: utf-8
# Questão: Empilhador de contêiner
# (C) 2018, Marcos Nascimento / UFCG, Teaching internship

EMPILHAR = "empilhar"
DESEMPILHAR = "desempilhar"
FIM_EXPEDIENTE = "fim de expediente"
ponteiro_pilha = 0

capacidade_maxima = int(raw_input())
if capacidade_maxima > 0:
	while True:
		acao = raw_input().lower()
		if acao == FIM_EXPEDIENTE:
			print "Navio está com {} conteiner(s).".format(ponteiro_pilha)
			break
		else:
			if acao == EMPILHAR:
				ponteiro_pilha += 1
				if ponteiro_pilha == capacidade_maxima:
					print "Navio está com carga completa."
					break
			if acao == DESEMPILHAR:
				if ponteiro_pilha == 0:
					print "Não há nenhum container no navio."
					break
				else:
					ponteiro_pilha -= 1 
