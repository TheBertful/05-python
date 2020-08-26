def smaller(a, b):
	print("Definindo o menor número entre %s e %s" % (a, b))
	if a < b:
		print("O número %s é o menor" % (a))
	elif a > b:
		print("O número %s é o menor" % (b))
	else:
		print("Os números são iguais")

smaller(1, 5)
smaller(4, 2)
smaller(5, 5)
