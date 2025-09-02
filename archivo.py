from archivo1 import saludo
from archivo2 import diccionario
from archivo3 import productos

print("***" * 40)


print(saludo)
print("*")
print(
    f"*NOMBRE:    {diccionario['NOMBRE :']}                                                                                   *")
print(
    f"*DIRECCION: {diccionario['DIRECCION :']}                                                                                   *")
print(
    f"*NIT:       {diccionario['NIT:']}                                                                                               *")
print(
    f"*TELEFONO:  {diccionario['TELEFONO:']}                                                                                              *")
print("*                                                                                                                      *")
print("*                                                                                                                      *")
print("*----------------------------------------------------------------------------------------------------------------------*")


print(f"*{'PRODUCTO':<15}{'CANTIDAD':>10}{'VALOR UNITARIO':>20}{'SUBTOTAL':>15}{'IVA':>10}{'TOTAL':>15}*")
print("*----------------------------------------------------------------------------------------------------------------------*")
