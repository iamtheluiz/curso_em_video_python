print("|*****************|")
print("|    Desafio11    |")
print("|*****************|")
print("")
print("Pintura em parede")
print("1L de tinta = 2 metros quadrados")
print();

alt = float(input("Digite a altura da parede (metros): "))
larg = float(input("Digite a largura da parede (metros): "))

area = alt*larg;

litros = area/2

print();
print("Sua parede tem {} metros quadrados".format(area))
print("Você precisa de {} Litros de tinta para pintar a parede!".format(litros))
