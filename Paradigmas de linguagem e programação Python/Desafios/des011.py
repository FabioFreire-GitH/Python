#Desafio 11 - Escreva um programa que leia a altura e largura de uma parede em metros,
#calcule a sua area e a quantidade de tinta necessaria para pintá-la, sabendo que,
#cada litro de tinta, pinta uma área de 2 metros quadrados.
print()
print('='*30)
print('Calculo de Área')
print('='*30)
print()
altura = float(input('Entre com a altura da parede: '))
print()
largura = float(input('Entre com a largura da paarete: '))
print()
area = (altura * largura)
qtd_tinta = area/2
print('A Área total da parade são: {:.2f} m² sendo necessário {:.2f} Litros de tinta para pintá-la'.format(area, qtd_tinta))
print()


