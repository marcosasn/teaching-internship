# coding: utf-8
# Questão: Casa de show
# (C) 2018, Marcos Nascimento / UFCG, Teaching internship

FEMININO = "f"
MASCULINO = "m"
FIM = "fim"
mulheres, homens = 0.0, 0.0

while True:
	sexo = raw_input().lower()
	if sexo == FIM:
		break
	else:
		if sexo == FEMININO:
			mulheres += 1
		elif sexo == MASCULINO:
			homens += 1

if mulheres + homens > 0:
	print "A porcentagem de mulheres é {:.2f}%".format(100*(mulheres/(mulheres + homens)))
	print "A porcentagem de homens é {:.2f}%".format(100*(homens/(mulheres + homens)))
else:
	print "A porcentagem de mulheres é {:.2f}%".format(mulheres)
	print "A porcentagem de homens é {:.2f}%".format(homens)
