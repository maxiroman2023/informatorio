print('----------------------------------------------------------------------------------------')
print('Bienvenid@ a InmobiliAPP: El mejor programa para automatizar la gestión de sus inmuebles') #Mensaje de Bienvenida
print('----------------------------------------------------------------------------------------')

def imprimir_lista(lista): #Función para imprimir la lista de modo ordenado y legible para el usuario
    j = 1
    for i in lista:
        print(f'N° {j}: {i}')
        j += 1

def validar_inmueble(item, valor): #Función para validar cada uno de los datos de un inmueble
    if item == 'año':
        if valor < 2000:
            print('No aceptamos inmuebles anteriores al año 2000')
            return False
        else: 
            return True
    if item == 'metros':
        if valor < 60:
            print('No aceptamos inmuebles de menos de 60 metros cuadrados')
            return False
        else:
            return True
    if item == 'habitaciones':
        if valor < 2:
            print('No aceptamos inmuebles con menos de 2 habitaciones')
            return False
        else:
            return True
    if item == 'garaje':
        if valor == '1' or valor == '2' or valor == '0':
            return True
        else:
            print('Ha ingresado un valor inválido')
            return False
    if item == 'zona':
        if valor == 'A' or valor == 'B' or valor == 'C' or valor == '0':
            return True
        else:
            print('Ha ingresado un valor inválido')
            return False
    if item == 'estado':
        if valor == '1' or valor == '2' or valor == '3' or valor == '0':
            return True
        else:
            print('Ha ingresado un valor inválido')
            return False

def agregar_inmueble(): #Función para agregar cada uno de los datos de un inmueble
        año = int(input('Ingrese el año: ')) #Pide ingreso del año
        while not validar_inmueble('año', año) and año != 0: #Pide ingreso mientras el dato no sea validado ni sea 0
            año = int(input('Ingrese nuevamente el año (si desea salir ingrese 0): ')) #Vuelve a pedir ingreso del dato
        metros = int(input('Ingrese la cantidad de metros cuadrados: ')) #Pide ingreso de los metros cuadrados
        while not validar_inmueble('metros', metros) and metros != 0: #Pide ingreso mientras el dato no sea validado ni sea 0
            metros = int(input('Ingrese nuevamente la cantidad de metros cuadrados (si desea salir ingrese 0): ')) #Vuelve a pedir ingreso del dato
        habitaciones = int(input('Ingrese la cantidad de habitaciones: ')) #Pide ingreso de la cantidad de habitaciones
        while not validar_inmueble('habitaciones', habitaciones) and habitaciones != 0: #Pide ingreso mientras el dato no sea validado ni sea 0
            habitaciones = int(input('Ingrese nuevamente las habitaciones (si desea salir ingrese 0): ')) #Vuelve a pedir ingreso del dato
        garaje = input('¿Tiene garaje? (1=Si 2=No): ') #Pide ingreso del dato mediante selección numérica
        while not validar_inmueble('garaje', garaje) and garaje != 0:
            garaje = input('Ingrese nuevamente si tiene garaje (1=Si 2=No 0=Salir): ')
        if garaje == '1':
            booleana = True #Si tiene garaje, la variable booleana adopta el valor True
        elif garaje == '2':
            booleana = False #Si no tiene garaje, la variable booleana adopta el valor False
        zona = input('Ingrese zona (A, B o C): ') #Pide ingreso del dato mediante selección alfabética
        while not validar_inmueble('zona', zona) and zona != 0:
            zona = input('Ingrese nuevamente la zona A, B o C (si desea salir ingrese 0): ')
        estado = input('Ingrese estado (1=Disponible 2=Reservado 3=Vendido): ') #Pide ingreso del dato mediante selección numérica
        while not validar_inmueble('estado', estado) and estado != 0:
            estado = input('Ingrese nuevamente estado (1=Disponible 2=Reservado 3=Vendido 0=Salir: ')
        if estado == '1':
            estado = 'Disponible' #Si se ingresa 1, el estado es "disponible"
        elif estado == '2':
            estado = 'Reservado' #Si se ingresa 2, el estado es "reservado"
        elif estado == '3':
            estado = 'Vendido' #Si se ingresa 3, el estado es "vendido"
        if año == 0 or metros == 0 or habitaciones == 0 or garaje == 0 or zona == 0 or estado == 0:
            return print('Ha ocurrido un error en la carga de datos')
        else: 
            inmueble = {'año': año, 'metros': metros, 'habitaciones': habitaciones, 'garaje': booleana, 'zona': zona, 'estado': estado}
            #Junta todos los datos ingresados en el diccionario "inmueble"
            return inmueble #Devuelve el diccionario creado

import datetime #Importo el módulo para manejo de fechas
fecha = datetime.date.today() #Le otorgo a fecha el valor de la fecha actual

def calcular_precio(inmueble): #Función para calcular el precio de un inmueble
    if inmueble['garaje']:
        garaje = 1
    else:
        garaje = 0
    if inmueble['zona'] == 'A':
        precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + garaje * 1500) * (1 - (fecha.year - inmueble['año']) / 100)
    if inmueble['zona'] == 'B':
        precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + garaje * 1500) * (1 - (fecha.year - inmueble['año']) / 100) * 1.5
    if inmueble['zona'] == 'C':
        precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + garaje * 1500) * (1 - (fecha.year - inmueble['año']) / 100) * 2
    return precio

def presupuesto(lista, precio_buscado): #Función para crear una nueva lista con los inmuebles que estpan por debajo de un precio
    otra_lista = []
    for i in lista:
        if calcular_precio(i) <= precio_buscado and i['estado'] == 'Disponible':
            otro_inmueble = i #hago una copia del inmueble para poder modificarlo sin cambiar el original
            otro_inmueble['precio'] = calcular_precio(otro_inmueble)
            otra_lista.append(otro_inmueble)
    return otra_lista

lista = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]
#Crea una lista de inmuebles con los datos de la consigna

opcion = 1 #Inicializa el selector de opciones

while opcion != '6': #Mientras la opción elegida no sea 6. Salir, ejecuta el bloque de código    
    opcion = (input('\n-_-=MENÚ PRINCIPAL=-_- \n1. Agregar un inmueble \n2. Editar un inmueble \n3. Eliminar un inmueble \n4. Cambiar el estado de un inmueble \n5. Buscar inmueble por presupuesto \n6. Salir \n\nElija una opción del menú: '))
    #Imprime menú de posibles operaciones
    
    if opcion == '1': #Si selecciona la opcion 1...
        print('\nHa elegido la opción 1: AGREGAR UN INMUEBLE')
        inmueble = agregar_inmueble() #Llama a la función agregar_inmueble
        lista.append(inmueble) #Agrega el nuevo diccionario "inmueble" a la lista de inmuebles 
        print('INMUEBLE AGREGADO CORRECTAMENTE\n') #Muestra mensaje de OK
    
    elif opcion == '2': #Si selecciona la opción 2...
        print('\nHa elegido la opción 2: EDITAR UN INMUEBLE\n') #¿CÓMO PODRÍA CONVERTIR ESTO EN UNA FUNCIÓN?
        print('Lista de inmuebles almacenados:') 
        imprimir_lista(lista) #Imprime la lista en un formato legible
        inmueble_a_editar = int(input('\nElija la posición numérica del inmueble a editar: ')) - 1
        #Pide ingresar la posición del inmueble a editar(-1 porque la primera posición siempre es 0)
        item_a_editar = input('Ingrese un ítem a editar (1=Año 2=Metros Cuadrados 3=Habitaciones 4=Garaje 5=Zona 6=Estado): ')
        #Pide ingresar el ítem a editar y ejecuta de acuerdo a la opción elegida
        if item_a_editar == '1': #Si el item a editar es "año":
            año = int(input('Ingrese nuevo año: ')) #Pide nuevo ingreso del dato
            if validar_inmueble(item_a_editar, año): #Llama a la función para validar el dato
                inmueble = lista[inmueble_a_editar] #Accedemos al inmueble a editar por su posición numérica
                inmueble['año'] = año #Cambia el valor del item "año" en el inmueble a editar
                lista[inmueble_a_editar] = inmueble #Vuelve a guardar el inmueble editado en la lista de inmuebles
                print('\nHa editado correctamente el ítem AÑO') #Imprime mensaje de edición correcta
        elif item_a_editar == '2': #Si el item a editar es "metros cuadrados"...
            metros = int(input('Ingrese nuevo valor de metros cuadrados: '))
            if validar_inmueble(item_a_editar, metros):
                inmueble = lista[inmueble_a_editar]
                inmueble['metros'] = metros
                lista[inmueble_a_editar] = inmueble
                print('\nHa editado correctamente el ítem METROS CUADRADOS')
        elif item_a_editar == '3': #Si el item a editar es "habitaciones"...
            habitaciones = int(input('Ingrese nuevo valor de habitaciones: '))
            if validar_inmueble(item_a_editar, habitaciones):
                inmueble = lista[inmueble_a_editar]
                inmueble['habitaciones'] = habitaciones
                lista[inmueble_a_editar] = inmueble
                print('\nHa editado correctamente el ítem HABITACIONES')
        elif item_a_editar == '4': #Si el item a editar es "garaje"...
            garaje = (input('Ingrese nuevamente si tiene garaje (1=Si 2=No): '))
            if validar_inmueble(item_a_editar, garaje):
                inmueble = lista[inmueble_a_editar]
                inmueble['garaje'] = garaje
                lista[inmueble_a_editar] = inmueble
                print('\nHa editado correctamente el ítem GARAJE')
        elif item_a_editar == '5': #Si el item a editar es "zona"...
            zona = (input('Ingrese nuevo valor de zona (A, B o C): '))
            if validar_inmueble(item_a_editar, zona):
                inmueble = lista[inmueble_a_editar]
                inmueble['zona'] = zona
                lista[inmueble_a_editar] = inmueble
                print('\nHa editado correctamente el ítem ZONA')
        elif item_a_editar == '6': #Si el item a editar es "estado"...
            estado = (input('Ingrese nuevo valor de estado (1=Disponible 2=Reservado 3=Vendido): '))
            if validar_inmueble(item_a_editar, estado):
                inmueble = lista[inmueble_a_editar]
                inmueble['estado'] = estado
                lista[inmueble_a_editar] = inmueble
                print('\nHa editado correctamente el ítem ESTADO')
    
    elif opcion == '3':
        print('\nHa elegido la opción 2: ELMINAR UN INMUEBLE\n')
        if lista == []: #Avisa si no hay inmuebles para eliminar
            print('Esta opción no está disponible porque aún no agregó ningún inmueble')
        else: 
            print('Lista de inmuebles almacenados:') #Imprime la lista de inmuebles almacenados
            imprimir_lista(lista)
            eliminado = int(input('\nElija la posición numérica del inmueble a eliminar: ')) - 1
            #Pide ingreso de la posición numérica del inmueble a eliminar (-1 porque la lista siempre comienza en 0)
            print(f'Usted va a eliminar este inmueble: \n{lista[eliminado]}')
            seguro = input('¿Está seguro? (1=Sí 2=No): ') #Pide confirmación antes de eliminar
            if seguro == '1':
                lista.remove(lista[eliminado]) #Si hay confirmación, elimina el inmueble de la lista
                print('Inmueble eliminado CORRECTAMENTE')
            elif seguro == '2':
                print('Ok. No lo eliminamos')
    
    elif opcion == '4':
        print('Ha elegido la opción 4: CAMBIAR EL ESTADO DE UN INMUEBLE')
        print('Lista de inmuebles almacenados:') 
        imprimir_lista(lista)
        inmueble_a_editar = int(input('\nElija la posición numérica del inmueble a editar: ')) - 1
        #Pide ingresar la posición del inmueble a editar(-1 porque la primera posición siempre es 0)
        estado = (input('Ingrese nuevo valor de estado (1=Disponible 2=Reservado 3=Vendido): '))
        if validar_inmueble('estado', estado): #Valida el ingreso de un valor correcto para "estado"
            inmueble = lista[inmueble_a_editar]
            if estado == '1':
                estado = 'Disponible' #Si se ingresa 1, el estado es "disponible"
            elif estado == '2':
                estado = 'Reservado' #Si se ingresa 2, el estado es "reservado"
            elif estado == '3':
                estado = 'Vendido' #Si se ingresa 3, el estado es "vendido"
            inmueble['estado'] = estado #Cambia el valor de estado
            lista[inmueble_a_editar] = inmueble #Vuelve a guardar el inmueble en la lista
            print('\nHa editado correctamente el ítem ESTADO')
            print(inmueble)
    
    elif opcion == '5':
        print('Ha elegido la opción 5: BUSCAR INMUEBLE POR PRESUPUESTO')
        precio = int(input('Ingrese el precio buscado: '))
        if presupuesto(lista, precio) == []:
            print('Por el momento, no se encuentran inmuebles disponibles por ese precio')
        else:
            print ('Los inmuebles disponibles por ese precio son los siguientes: ')
            imprimir_lista(presupuesto(lista, precio))
        
    elif opcion < '1' or opcion > '6':
        print('No ha ingresado una opción válida. Vuelva a intentarlo')

print('\n-------------------------------------------')
print('Gracias por usar InmobiliAPP. Hasta pronto!') #Mensaje de despedida
print('-------------------------------------------')