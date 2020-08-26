def show_numbers(limit):
	for i in range(limit+1):
		print("* {} {}".format(i, append_odd_even(i)))

def append_odd_even(number):
	if number % 2 == 0:
		return "PAR"
	else:
		return "IMPAR"


show_numbers(100)
