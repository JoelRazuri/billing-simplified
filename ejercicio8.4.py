"""
    # Sistema de facturación simplificado:
    
    Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de (identificador, descripción, precio), y una lista de los productos a facturar, en la que cada uno 
    consiste en una tupla de (identificador, cantidad).
    Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el precio total de cada producto comprado, y al final imprima el total general. Escribir una 
    función que reciba ambas listas e imprima por pantalla la factura solicitada.
"""

import pprint

lista_productos = [
        (1, 'Remera Nike', 120),
        (2, 'Zapatillas Gucci', 150.5),
        (3, 'Reloj', 500),
        (4, 'Cepillo de dientes', 100),
        (5, 'Gorra', 70.9),
        (6, 'Pelota de Futbol', 15),
        (7, 'Botines de F11', 25.5)
    ]


lista_productos_facturar = [
        (2, 1),
        (4, 5),
        (1, 3),
        (6, 10),
        (3, 2)
]



def facturacion_simple(lista_produc, lista_produc_facturar):

    total_general = 0

    print(
        "              -------- FACTURA --------\n"
        "CANTIDAD    DESCRIPCIÓN    PRECIO UNITARIO    PRECIO TOTAL"  
    )

    for i in range(0, len(lista_produc_facturar)):

        iden_facturados = lista_produc_facturar[i][0]
        
        for j in range(0,len(lista_produc)):

            iden_produc = lista_produc[j][0]

            if iden_facturados == iden_produc:
                cantidad = lista_produc_facturar[i][1]
                descripcion = lista_produc[i][1]
                precio_unitario = lista_produc[i][2]
                precio_total = cantidad * precio_unitario
                total_general = total_general + precio_total

        print(f"    {cantidad}          {descripcion}            $ {precio_unitario}            $ {precio_total}")
            

    print(f"\nTOTAL GENERAL: $ {total_general}")




facturacion_simple(lista_productos,lista_productos_facturar)




