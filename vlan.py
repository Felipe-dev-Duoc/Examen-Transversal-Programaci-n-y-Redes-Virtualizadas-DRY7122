NORMAL = range(1, 1006)
EXTENDIDO = range(1006, 4095)

vlan = int(input("Por favor, ingrese el número de VLAN: "))

if vlan in NORMAL:
    print("La VLAN {} esta entre rango normal.".format(vlan))
elif vlan in EXTENDIDO:
    print("La VLAN {} esta entre rango extendido.".format(vlan))
else:
    print("El número de VLAN {} no es válido.".format(vlan))