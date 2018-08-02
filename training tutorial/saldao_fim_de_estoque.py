#coding: utf-8
#Marcos Nascimento, 2018

FIM = "fim"
MINIMO_DESCONTO = 50.0
cont_produtos = 0
preco_total, preco_desconto = 0.0, 0.0

while True:
	entrada = raw_input()
	if entrada.lower() == FIM:
		break
	else:
		produto, preco_produto = entrada.split(" ")
		if produto:
			cont_produtos += 1
		if float(preco_produto) > MINIMO_DESCONTO:
			preco_total += float(preco_produto)
			preco_produto = (float(preco_produto) - (float(preco_produto)*.4))
			preco_desconto += preco_produto
		else:
			preco_total += float(preco_produto)
			preco_desconto += float(preco_produto)

print "Total de produtos: {}".format(cont_produtos)
print "Preço total: R$ {:.2f}".format(preco_total)
print "Total com desconto: R$ {:.2f}".format(preco_desconto)