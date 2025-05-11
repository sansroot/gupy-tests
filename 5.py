def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

entrada = input("Informe uma string para inverter: ")
print(f"String invertida: {inverter_string(entrada)}")
