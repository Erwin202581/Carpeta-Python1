VARA = 1
VARB = 1
VARC = 1
VARD = 1
VARE = 1
VARF = 1
VARG = 1

# Lista de diccionarios con patrones
patrones = [
    {"patron": (1, 1, 1, 1, 1, 1, 0), "numero": 0},
    {"patron": (0, 1, 1, 0, 0, 0, 0), "numero": 1},
    {"patron": (1, 1, 1, 1, 1, 0, 1), "numero": 2},
    {"patron": (1, 1, 1, 1, 0, 0, 1), "numero": 3},
    {"patron": (0, 1, 1, 0, 0, 1, 1), "numero": 4},
    {"patron": (1, 0, 1, 1, 0, 1, 1), "numero": 5},
    {"patron": (1, 0, 1, 1, 1, 1, 1), "numero": 6},
    {"patron": (1, 0, 1, 0, 0, 0, 0), "numero": 7},
    {"patron": (1, 1, 1, 1, 1, 1, 1), "numero": 8},
    {"patron": (1, 1, 1, 1, 0, 1, 1), "numero": 9},
]

# Entrada actual
entrada = (VARA, VARB, VARC, VARD, VARE, VARF, VARG)

# Recorremos la lista con for
encontrado = False
for item in patrones:
    if entrada == item["patron"]:
        print(f"Este valor es {item['numero']}")
        encontrado = True
        break

if not encontrado:
    print("Este valor NO es correcto")
