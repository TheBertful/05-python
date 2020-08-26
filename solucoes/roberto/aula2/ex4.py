def check_sum():
	a = int(input("Insira o primeiro número: "))
	b = int(input("Insira o segundo número: "))
	s = a + b
	if s > 20:
		s += 8
	else:
		s -= 5
	print(s)

check_sum()
