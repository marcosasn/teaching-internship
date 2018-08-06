# coding: utf-8
# Questão: Trabalho de pesquisa
# (C) 2018, Marcos Nascimento / UFCG, Teaching internship

todas_infos = dict()
FIM = "fim"
CONTRA = "Contra"
AFAVOR = "A favor"
conta_contra, conta_afavor, conta_neutro = 0.0, 0.0, 0.0

def ordenar_infos(todos_nomes):
    for j in range(len(todos_nomes)-1,0,-1):
        for i in range(j):
            if todos_nomes[i] > todos_nomes[i+1]:
                temp = todos_nomes[i]
                todos_nomes[i] = todos_nomes[i+1]
                todos_nomes[i+1] = temp
    return todos_nomes
				 
while True:
	nome = raw_input() 
	if nome == FIM:
		break
	else:
		telefone = raw_input()
		email = raw_input()
		voto = raw_input()
		todas_infos[nome] = [email, telefone, voto]

if len(todas_infos.keys()) > 0:
	for nome in ordenar_infos(todas_infos.keys()):
		print("Nome: %s" % nome)
		print("Telefone: %s" % todas_infos[nome][1])
		print("E-mail: %s" % todas_infos[nome][0])
		print("Voto: %s" % todas_infos[nome][2])
		print("----------------------")
		if todas_infos[nome][2] == CONTRA:
			conta_contra += 1
		elif todas_infos[nome][2] == AFAVOR:
			conta_afavor += 1
		else:
			conta_neutro += 1

	print "Estatísticas da Pesquisa"
	print "----------------------"
	print "{} Participante(s) votaram a favor, significando ({:.2f}%) dos votos.".format(int(conta_afavor), (conta_afavor/len(todas_infos.keys())*100))
	print "{} Participante(s) votaram contra, significando ({:.2f}%) dos votos.".format(int(conta_contra), (conta_contra/len(todas_infos.keys())*100))
	print "{} Participante(s) votaram neutro, significando ({:.2f}%) dos votos.".format(int(conta_neutro), (conta_neutro/len(todas_infos.keys())*100))
else:
	print "Estatísticas da Pesquisa"
	print "----------------------"
	print "{} Participante(s) votaram a favor, significando ({:.2f}%) dos votos.".format(int(conta_afavor), conta_afavor)
	print "{} Participante(s) votaram contra, significando ({:.2f}%) dos votos.".format(int(conta_contra), conta_contra)
	print "{} Participante(s) votaram neutro, significando ({:.2f}%) dos votos.".format(int(conta_neutro), conta_neutro)
