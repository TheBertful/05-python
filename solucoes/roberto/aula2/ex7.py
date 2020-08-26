def show_month_name():
	month = int(input("Insira o número do mês: "))
	month_list = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
	if month in range(1, len(month_list) + 1):
		print("O mês {} é {}".format(month, month_list[month-1]))
	else:
		print("Não existe mês {}.".format(month))

show_month_name()
