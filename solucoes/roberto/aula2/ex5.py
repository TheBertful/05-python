import math

def sq_or_sqrt():
	a = int(input("Insira o número: "))
	if a >= 0:
		print(math.sqrt(a))

	else:
		print(a ** 2)

sq_or_sqrt()
