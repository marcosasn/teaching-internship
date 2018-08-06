# coding: utf-8
# Questão: Saldao fim de estoque
# (C) 2018, Marcos Nascimento / UFCG, Teaching internship

FIM = "fim"
PRECO_DESCONTO = 50.0
produtos = 0
preco_total, preco_desconto = 0.0, 0.0

while True:
	entrada = raw_input().lower()
	if entrada == FIM:
		break
	else:
		produto, preco_produto = entrada.split(" ")
		if produto:
			produtos += 1
		if float(preco_produto) > PRECO_DESCONTO:
			preco_total += float(preco_produto)
			preco_produto = (float(preco_produto) - (float(preco_produto)*.4))
			preco_desconto += preco_produto
		else:
			preco_total += float(preco_produto)
			preco_desconto += float(preco_produto)

print "Total de produtos: {}".format(produtos)
print "Preço total: R$ {:.2f}".format(preco_total)
print "Total com desconto: R$ {:.2f}".format(preco_desconto)