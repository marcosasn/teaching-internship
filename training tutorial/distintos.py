#coding: utf-8
#Marcos Nascimento, 2018

def distintos(numero):
	unicos = 0
	digitos = dict()
	for digito in str(numero):
		digitos[digito] = 0

	for digito in str(numero):
		digitos[digito] += 1

	for digito in digitos.keys():
		if digitos[digito] == 1:
			unicos += 1
	return unicos

numero = raw_input()
print distintos(numero)








