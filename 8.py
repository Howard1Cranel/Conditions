year = int(input("Введите год: "))
if year % 4 == 0:
	print(year, "-ый год является високосным, в нём 366 дней")
else:
	print(year, "-ый год не является високосным, в нём 365 дней")