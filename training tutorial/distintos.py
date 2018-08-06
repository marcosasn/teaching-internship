# coding: utf-8
# Questão: Números distintos
# (C) 2018, Marcos Nascimento / UFCG, Teaching internship

def distintos(numero):
	unicos = 0
	digitos = dict()

	for digito in str(numero):
		if digito in digitos.keys():
			digitos[digito] += 1
		else:
			digitos[digito] = 1

	for digito in digitos.keys():
		if digitos[digito] == 1:
			unicos += 1
	return unicos

numero = raw_input()
print distintos(numero)








