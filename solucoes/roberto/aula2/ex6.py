def check_speed(speed):
	print("Velocidade: {}".format(speed))
	if speed <= 70:
		print("Ok")
	else:
		points = (speed - 70) // 5
		if points > 12:
			print("License suspended")
		else:
			print("Caraca bicho, {} pontos".format(points))

check_speed(50)
check_speed(70)
check_speed(123)
check_speed(250)
