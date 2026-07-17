import datetime

data = datetime.date(2026, 1 ,5)
print(data)

hora= datetime.time(18, 15, 22)
print(hora)

print(datetime.datetime(2026, 1, 5, 18, 15, 22))
print(data, hora)

instante = (datetime.datetime(2026, 1, 5, 18, 15, 22))
print(instante.strftime('Dia %d/%m/%Y, às %H horas e %M minutos.'))

print()

texto = "2023-12-31T08:45:30"

data = datetime.datetime.strptime(texto, '%Y-%m-%dT%H:%M:%S')
print(data)

hoje = datetime.datetime.today()

ano_2000 = datetime.datetime(2000, 1, 1)

diferenca = hoje - ano_2000

print(diferenca) #.timedelta

print(diferenca.total_seconds())