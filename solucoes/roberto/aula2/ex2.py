def isdonator():
	age = int(input("Informe sua idade: "))
	weight = int(input("Informe agora seu peso em kg: "))
	hours = int(input("Por fim, informe quantas horas dormiu nas últimas 24 horas: "))
	message = []
	if not check_age(age):
		message.append("Precisa ter entre 16 e 69 anos.")
	if not check_weight(weight):
		message.append("Precisa pesar mais de 50kg.")
	if not check_hours(hours):
		message.append("Precisa ter dormido ao menos 6 horas nas últimas 24 horas.")
	if len(message) > 0:
		print("Não pode doar pelos seguintes motivos:")
		print("\n".join(message))
	else:
		print("Pode doar sem problemas.")

def check_age(age):
	return age >= 16 and age <= 69

def check_weight(weight):
	return weight > 50

def check_hours(hours):
	return  hours >= 6


isdonator()
