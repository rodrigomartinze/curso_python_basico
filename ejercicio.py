from datetime import datetime;
#1-FACTURACION MEDIA DE TRES EMPRESAS
def facturacion(e1,e2,e3):
    media = (e1 + e2 + e3) / 3
    print("La media es: ", media)

facturacion(100,200,300)

#2-FACTURACION MEDIA DE MAS DE TRES EMPRESAS

def facturacion(empresas):
    suma = sum(empresas)
    media = suma / len(empresas)
    print("La media es: ", media)


facturacion([150,240,344,235,342,543,215,853,234])

#3-CALCULAR PRECIO DE UNA COMPRA CON IMPUESTOS DE 21 Y MOSTRAR AL FINAL DEL BUCLE TODOS LOS DATOS COMO PRECIO UNITARIO
#TOTA, IMPUESTO, ETC, EL COMPRADOR PODRA ELEJIR LOS DISTINTOS ARTICULOS Y LA CANTIDAD DE ELLOS.

nombre = input("Nombre del comprador: ")
precio_unitario = [15, 8.5, 40, 28.9, 2.4, 24.3,18,2, 12, 9.5, 13.5]
productos = ["Leche", "Pan", "Queso", "Mantequilla", "Jamon", "Cereales", "Galletas", "Azucar", "Harina", "Arroz"]
opc = 1
carrito = []

def sumar_carrito():
    pass


while opc !=0 :
    opc = int(input("1-Leche /n2-Pan /n3-Queso /n4-Mantequilla /n5-Jamon /n6-Cereales /n7-Galletas /n8-Azucar /n9-Harina /n10-Arroz /n0-Salir \nElige un producto: "))
    if opc == 0:
        break
    elif opc > 10:
        print("Opcion no valida")
    else:
        cantidad = int(input("Cuantos quieres? "))
        precio = precio_unitario[opc - 1] * cantidad
        carrito.append(precio)
        carrito.append(productos[opc - 1])

total = sum(carrito[::2])

print("-------------------------------------------------------")
print("Factura de compra")
print(f"Buenas tardes {nombre}")
print("fecha realizada: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Productos comprados:")
for i in range(0, len(carrito), 2):
    print(f"{carrito[i+1]} - {carrito[i]:.2f}")
print("Total sin IVA: ", total)
print("Total con IVA: ", total * 1.21)
print("-------------------------------------------------------")
print("Gracias por su compra")


