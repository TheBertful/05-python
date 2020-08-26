def roots(a, b, c):
	print("Coeficientes A=%.4f, B=%.4f, C=%.4f" % (a, b, c))
	print("Verificando validade da equação de segundo grau:")
	if a == 0:
		print("Equação inválida. Coeficiente A não pode ser zero.")
	else:
		print("Calculando valor do Delta:")
		dlt = delta(a, b, c)
		print("Delta: {:.4f}".format(dlt))
		if dlt > 0:
			print("Possui duas raízes reais diferentes.")
		elif dlt == 0:
			print("Possui apenas uma raiz real.")
		else:
			print("Não possui nenhuma raiz real.")

def delta(a, b, c):
	return (b ** 2) - (4 * a * c)

roots(4, 4, 1) # Delta = 0
roots(1, 2, 4) # Delta < 0
roots(1, 5, 1) # Delta > 0
roots(0, 5, 2) # Não é 2º grau
