#Desafio 14 - Conversor de Temperaturas. Celsius para Fahrenheit.
print()
print('='*30)
print('Calculo de Conversão de Temperatura')
print('='*30)
print()
cel = float(input('Enrte do a temperatura em Celsius(°C): '))
print('\nTemperatura digitada: {:.1f}°C')
fah = (cel * 1.8) + 32 # ou (cel * 9/5) + 32 ou ((9*cel) / 5) +32
print('\nA temperatua {:.1f}°C em fahrenheit é: {:.1f}°F'.format(cel, fah))
print()
