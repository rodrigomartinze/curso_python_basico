#1-FACTURACION MEDIA DE TRES EMPRESAS
def facturacion(e1,e2,e3):
    media = (e1 + e2 + e3) / 3
    print("La media es: ", media)

facturacion(100,200,300)

#FACTURACION MEDIA DE MAS DE TRES EMPRESAS

def facturacion(empresas):
    suma = sum(empresas)
    media = suma / len(empresas)
    print("La media es: ", media)


facturacion([150,240,344,235,342,543,215,853,234])