import MongoHandler
from Models import Galaxia, SistemaSolar, Estrella, Planeta, Luna

db_handler = MongoHandler.MongoHandler("mongodb+srv://admin:admin@universbd.dxuaa8n.mongodb.net/?retryWrites=true&w=majority")

# # # # # # # # # # # # # # #
# |--galaxias               #
#   |-- sistemas solares    #
#     |-- estrellas         #
#     |-- planetas          #
#       |-- lunas           #
# # # # # # # # # # # # # # #

# Menu principal
def main_menu():
    print('\n/=========================\\')
    print('| (1) Mostrar galaxias    |')
    print('| (2) Seleccionar galaxia |')
    print('| (3) Añadir galaxia      |')
    print('| (0) Salir               |')
    print('\=========================/')
    opcion = input('->> ')

    if opcion == '1':
        db_handler.imprimir_nombres_documento("galaxies")
    elif opcion == '2':
        get_galaxia()
    elif opcion == '3':
        anadir_galaxia()
    elif opcion == '0':
        exit()
    else:
        print('\n¡¡¡ Opcion no valida !!!')
        main_menu()

# GET GALAXIA
def get_galaxia():
    db_handler.imprimir_nombres_documento("galaxies")
    opcion = input('->> ')
    if db_handler.existe_documento("galaxies", opcion):
        galaxia(opcion)
    else:
        main_menu()

# CREATE GALAXIA
def anadir_galaxia():
    data = {
        "name": input('Nombre->> '),
        "type": input('Tipo->> '),
        "distance_ly": int(input('Distancia al planeta Tierra->> ')),
        "num_stars": int(input('Numero de estrellas->> ')),
        "num_planets": int(input('Numero de planetas->> ')),
    }
    db_handler.anadir_documento("galaxies", data)
    main_menu()

# READ GALAXIA
def mostrar_galaxia(galaxia_obj: Galaxia):
    db_handler.imprimir_documento("galaxies", galaxia_obj._id)
    galaxia(galaxia_obj.name)

# UPDATE GALAXIA
def modificar_galaxia(galaxia_obj: Galaxia):
    db_handler.modificar_documento("galaxies", galaxia_obj._id, {
        "name": input('Nombre->> '),
        "type": input('Tipo->> '),
        "distance_ly": int(input('Distancia al planeta Tierra->> ')),
        "num_stars": int(input('Numero de estrellas->> ')),
        "num_planets": int(input('Numero de planetas->> ')),
    })
    main_menu()

# DELETE GALAXIA
def eliminar_galaxia(galaxia_obj: Galaxia):
    db_handler.eliminar_documento("galaxies", galaxia_obj._id)
    main_menu()


# Menu galaxia
def galaxia(galaxia_nombre):
    galaxia_data = db_handler.get_documento("galaxies", galaxia_nombre)
    galaxia_obj = Galaxia(
        galaxia_data['_id'], 
        galaxia_data['name'], 
        galaxia_data['type'], 
        galaxia_data['distance_ly'], 
        galaxia_data['num_stars'], 
        galaxia_data['num_planets']
    )

    print('\nGALAXIA: ' + galaxia_obj.name)
    print('/=========================\\')
    print('| (1) Mostrar sistemas    |')
    print('| (2) Seleccionar sistema |')
    print('| (3) Añadir sistema      |')
    print('| (4) Mostrar galaxia     |')
    print('| (5) Modificar galaxia   |')
    print('| (6) Eliminar galaxia    |')
    print('| (0) Atras               |')
    print('\=========================/')
    opcion = input('->> ')

    if opcion == '1':
        db_handler.imprimir_nombres_documento("sistemas_solar")
    elif opcion == '2':
        get_sistema(galaxia_obj)  
    elif opcion == '3':
        anadir_sistema(galaxia_obj)
    elif opcion == '4':
        mostrar_galaxia(galaxia_obj)
    elif opcion == '5':
        modificar_galaxia(galaxia_obj)
    elif opcion == '6':
        eliminar_galaxia(galaxia_obj)
    elif opcion == '0':
        main_menu()
    else:
        print('\n¡¡¡ Opcion no valida !!!')
        galaxia(galaxia_nombre)


# GET SISTEMA SOLAR
def get_sistema(galaxia_obj: Galaxia):
    db_handler.imprimir_nombres_documento("solar_systems", {"ref_galaxy": galaxia_obj._id})
    opcion = input('->> ')
    if db_handler.existe_documento("solar_systems", {"name": opcion, "ref_galaxy": galaxia_obj._id}):
        sistema_solar(opcion, galaxia_obj)
    else:
        galaxia(galaxia_obj.name)

# CREATE SISTEMA SOLAR
def anadir_sistema(galaxia_obj: Galaxia):
    data = {"name": input('Nombre->> '),
            "galaxy":galaxia_obj.name,
            "num_planets":{"$numberInt": input('Numero de planetas->> ')},
            "num_stars":{"$numberInt": input('Numero de estrellas->> ')},
            "ref_galaxy":galaxia_obj._id}
    db_handler.anadir_documento("solar_systems", data)
    galaxia(galaxia_obj.name)

# READ SISTEMA SOLAR
def mostrar_sistema(sistema_obj: SistemaSolar):
    db_handler.imprimir_documento("solar_systems", sistema_obj._id)
    sistema_solar(sistema_obj.name)

# UPDATE SISTEMA SOLAR
def modificar_sistema(sistema_obj: SistemaSolar, galaxia_obj: Galaxia):
    db_handler.modificar_documento("solar_systems", sistema_obj._id, {"name": input('Nombre->> '),
            "num_planets":{"$numberInt": input('Numero de planetas->> ')},
            "num_stars":{"$numberInt": input('Numero de estrellas->> ')}
            })
    galaxia(galaxia_obj.name)

# DELETE SISTEMA SOLAR
def eliminar_sistema(galaxia_obj: Galaxia):
    db_handler.eliminar_documento("galaxies", galaxia_obj._id)
    galaxia(galaxia_obj.name)


# Menu sistema
def sistema_solar(sistema_nombre, galaxia_obj: Galaxia):
    sistema_data = db_handler.get_documento("solar_systems", sistema_nombre)
    sistema_obj = SistemaSolar(
        sistema_data['_id'], 
        sistema_data['name'], 
        sistema_data['ref_galaxy']
    )

    print('\nSISTEMA: ' + sistema_obj.name)
    print('/=========================\\')
    print('| (1) Mostrar estrellas   |')
    print('| (2) Mostrar planetas    |')
    print('| (3) Seleccionar estrella|')
    print('| (4) Seleccionar planeta |')
    print('| (5) Añadir estrella     |')
    print('| (6) Añadir planeta      |')
    print('| (7) Mostrar sistema     |')
    print('| (8) Modificar sistema   |')
    print('| (9) Eliminar sistema    |')
    print('| (0) Atras               |')
    print('\=========================/')

    opcion = input('->> ')

    if opcion == '1':
        db_handler.imprimir_nombres_documento("sistemas_solar")
    elif opcion == '2':
        get_sistema(galaxia_obj)  
    elif opcion == '3':
        pass
    elif opcion == '4':
        mostrar_galaxia(galaxia_obj)
    elif opcion == '5':
        modificar_galaxia(galaxia_obj)
    elif opcion == '6':
        eliminar_galaxia(galaxia_obj)
    elif opcion == '7':
        mostrar_sistema(sistema_obj)
    elif opcion == '8':
        modificar_sistema(sistema_obj)
    elif opcion == '9':
        eliminar_sistema(sistema_obj)
    elif opcion == '0':
        main_menu()
    else:
        print('\n¡¡¡ Opcion no valida !!!')
        sistema_solar(sistema_obj.name, galaxia_obj)



main_menu()