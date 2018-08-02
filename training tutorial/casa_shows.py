#coding: utf-8
#Marcos Nascimento, 2018

FEMININO = "F"
MASCULINO = "M"
FIM = "fim"
sexo_feminino, sexo_masculino = 0.0, 0.0

while True:
	sexo = raw_input()
	if sexo.lower() == FIM:
		break
	else:
		if sexo.upper() == FEMININO:
			sexo_feminino += 1
		elif sexo.upper() == MASCULINO:
			sexo_masculino += 1

print "A porcentagem de mulheres é {:.2f}%".format(100*(sexo_feminino/(sexo_feminino + sexo_masculino)))
print "A porcentagem de homens é {:.2f}%".format(100*(sexo_masculino/(sexo_feminino + sexo_masculino)))
