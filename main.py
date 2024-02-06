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
    while True:
        print('\n/=========================\\')
        print('| (1) Mostrar galaxias    |')
        print('| (2) Seleccionar galaxia |')
        print('| (3) Añadir galaxia      |')
        print('| (0) Salir               |')
        print('\=========================/')
        opcion = input('->> ')

        if opcion == '1':
            db_handler.imprimir_nombres_documento("galaxies", {})
        elif opcion == '2':
            get_galaxia()
        elif opcion == '3':
            anadir_galaxia()
        elif opcion == '0':
            exit()
        else:
            print('\n¡¡¡ Opcion no valida !!!')










# GET GALAXIA
def get_galaxia():
    db_handler.imprimir_nombres_documento("galaxies", {})
    opcion = input('->> ')
    if db_handler.existe_documento("galaxies", opcion, {}):
        galaxia(opcion)
    else:
        print('\n¡¡¡ Galaxia no encontrada !!!')

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

# READ GALAXIA
def mostrar_galaxia(galaxia_obj: Galaxia):
    db_handler.imprimir_documento("galaxies", galaxia_obj._id)

# UPDATE GALAXIA
def modificar_galaxia(galaxia_obj: Galaxia):
    db_handler.modificar_documento("galaxies", galaxia_obj._id, {
        "name": input('Nombre->> '),
        "type": input('Tipo->> '),
        "distance_ly": int(input('Distancia al planeta Tierra->> ')),
        "num_stars": int(input('Numero de estrellas->> ')),
        "num_planets": int(input('Numero de planetas->> ')),
    })

# DELETE GALAXIA
def eliminar_galaxia(galaxia_obj: Galaxia):
    db_handler.eliminar_documento("galaxies", galaxia_obj._id)

# Menu galaxia
def galaxia(galaxia_nombre):
    while True:
        galaxia_data = db_handler.get_documento("galaxies", galaxia_nombre)
        galaxia_obj = Galaxia(
            str(galaxia_data['_id']), 
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
            db_handler.imprimir_nombres_documento("solar_systems", {"ref_galaxy": galaxia_obj._id})
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
            break
        else:
            print('\n¡¡¡ Opcion no valida !!!')










# GET SISTEMA SOLAR
def get_sistema(galaxia_obj: Galaxia):
    db_handler.imprimir_nombres_documento("solar_systems", {"ref_galaxy": galaxia_obj._id})
    opcion = input('->> ')
    if db_handler.existe_documento("solar_systems", opcion, {"ref_galaxy": galaxia_obj._id}):
        sistema_solar(opcion, galaxia_obj)
    else:
        print('\n¡¡¡ Sistema solar no encontrado !!!')

# CREATE SISTEMA SOLAR
def anadir_sistema(galaxia_obj: Galaxia):
    data = {"name": input('Nombre->> '),
            "galaxy":galaxia_obj.name,
            "num_planets":{"$numberInt": input('Numero de planetas->> ')},
            "num_stars":{"$numberInt": input('Numero de estrellas->> ')},
            "ref_galaxy":galaxia_obj._id}
    db_handler.anadir_documento("solar_systems", data)

# READ SISTEMA SOLAR
def mostrar_sistema(sistema_obj: SistemaSolar):
    db_handler.imprimir_documento("solar_systems", sistema_obj._id)

# UPDATE SISTEMA SOLAR
def modificar_sistema(sistema_obj: SistemaSolar):
    db_handler.modificar_documento("solar_systems", sistema_obj._id, {"name": input('Nombre->> '),
            "num_planets":{"$numberInt": input('Numero de planetas->> ')},
            "num_stars":{"$numberInt": input('Numero de estrellas->> ')}
            })

# DELETE SISTEMA SOLAR
def eliminar_sistema(sistema_obj: SistemaSolar):
    db_handler.eliminar_documento("solar_systems", sistema_obj._id)

# Menu sistema
def sistema_solar(sistema_nombre, galaxia_obj: Galaxia):
    while True:
        sistema_data = db_handler.get_documento("solar_systems", sistema_nombre)
        sistema_obj = SistemaSolar(
            str(sistema_data['_id']), 
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
            db_handler.imprimir_nombres_documento("stars", {"ref_solar_system": sistema_obj._id})
        elif opcion == '2':
            db_handler.imprimir_nombres_documento("planets", {"ref_solar_system": sistema_obj._id})
        elif opcion == '3':
            get_estrella(sistema_obj)
        elif opcion == '4':
            get_planeta(sistema_obj)
        elif opcion == '5':
            anadir_estrella(sistema_obj)
        elif opcion == '6':
            anadir_planeta(sistema_obj)
        elif opcion == '7':
            mostrar_sistema(sistema_obj)
        elif opcion == '8':
            modificar_sistema(sistema_obj)
        elif opcion == '9':
            eliminar_sistema(sistema_obj)
        elif opcion == '0':
            break
        else:
            print('\n¡¡¡ Opcion no valida !!!')










# GET ESTRELLA
def get_estrella(sistema_obj: SistemaSolar):
    db_handler.imprimir_nombres_documento("stars", {"ref_solar_system": sistema_obj._id})
    opcion = input('->> ')
    if db_handler.existe_documento("stars", opcion, {"ref_solar_system": sistema_obj._id}):
        estrella(opcion, sistema_obj)
    else:
        print('\n¡¡¡ Estrella no encontrada !!!')

# CREATE ESTRELLA
def anadir_estrella(sistema_obj: SistemaSolar):
    data = {"name": input('Nombre->> '),
            "type": input('Tipo->> '),
            "mass_kg": input('Masa->> '),
            "radius_km": input('Radio->> '),
            "temperature_kelvin": input('Temperatura->> '),
            "solar_system": sistema_obj.name,
            "ref_solar_system": sistema_obj._id
        }
    db_handler.anadir_documento("stars", data)
    
# READ ESTRELLA
def mostrar_estrella(estrella_obj: Estrella):
    db_handler.imprimir_documento("stars", estrella_obj._id)

# UPDATE ESTRELLA
def modificar_estrella(estrella_obj: Estrella):
    db_handler.modificar_documento("stars", estrella_obj._id, {"name": input('Nombre->> '),
            "type": input('Tipo->> '),
            "mass_kg": input('Masa->> '),
            "radius_km": input('Radio->> '),
            "temperature_kelvin": input('Temperatura->> ')
        })

# DELETE ESTRELLA
def eliminar_estrella(estrella_obj: Estrella):
    db_handler.eliminar_documento("stars", estrella_obj._id)

# Menu estrella
def estrella(estrella_nombre, sistema_obj: SistemaSolar):
    while True:
        estrella_data = db_handler.get_documento("stars", estrella_nombre)
        estrella_obj = Estrella(
            str(estrella_data['_id']), 
            estrella_data['name'], 
            estrella_data['ref_solar_system']
        )

        print('\nESTRELLA: ' + estrella_obj.name)
        print('/=========================\\')
        print('| (1) Mostrar estrella     |')
        print('| (2) Modificar estrella   |')
        print('| (3) Eliminar estrella    |')
        print('| (0) Atras                |')
        print('\=========================/')

        opcion = input('->> ')

        if opcion == '1':
            mostrar_estrella(estrella_obj)
        elif opcion == '2':
            modificar_estrella(estrella_obj)
        elif opcion == '3':
            eliminar_estrella(estrella_obj)
        elif opcion == '0':
            break
        else:
            print('\n¡¡¡ Opcion no valida !!!')










# GET PLANETA
def get_planeta(sistema_obj: SistemaSolar):
    db_handler.imprimir_nombres_documento("planets", {"ref_solar_system": sistema_obj._id})
    opcion = input('->> ')
    if db_handler.existe_documento("planets", opcion, {"ref_solar_system": sistema_obj._id}):
        planeta(opcion, sistema_obj)
    else:
        print('\n¡¡¡ Planeta no encontrado !!!')

# CREATE PLANETA
def anadir_planeta(sistema_obj: SistemaSolar):
    data = {"name": input('Nombre->> '),
            "type": input('Tipo->> '),
            "diameter_km": input('Diametro->> '),
            "mass_kg": input('Masa->> '),
            "moons": input('Lunas->> '),
            "atmosphere": input('Atmosfera->> '),
            "orbital_period_days": input('Periodo orbital->> '),
            "temperature_avg_celsius": input('Temperatura media->> '),
            "solar_system": sistema_obj.name,
            "ref_solar_system": sistema_obj._id}
    db_handler.anadir_documento("planets", data)
    
# READ PLANETA
def mostrar_planeta(planeta_obj: Planeta):
    db_handler.imprimir_documento("planets", planeta_obj._id)

# UPDATE PLANETA
def modificar_planeta(planeta_obj: Planeta):
    db_handler.modificar_documento("planets", planeta_obj._id, {"name": input('Nombre->> '),
            "type": input('Tipo->> '),
            "diameter_km": input('Diametro->> '),
            "mass_kg": input('Masa->> '),
            "moons": input('Lunas->> '),
            "atmosphere": input('Atmosfera->> '),
            "orbital_period_days": input('Periodo orbital->> '),
            "temperature_avg_celsius": input('Temperatura media->> ')
        })

# DELETE PLANETA
def eliminar_planeta(planeta_obj: Planeta):
    db_handler.eliminar_documento("planets", planeta_obj._id)

# Menu planetas
def planeta(planeta_nombre, sistema_obj: SistemaSolar):
    while True:
        planeta_data = db_handler.get_documento("planets", planeta_nombre)
        planeta_obj = Planeta(
            str(planeta_data['_id']), 
            planeta_data['name'], 
            planeta_data['ref_solar_system']
        )

        print('\nPLANETA: ' + planeta_obj.name)
        print('/=========================\\')
        print('| (1) Mostrar lunas       |')
        print('| (2) Seleccionar luna    |')
        print('| (3) Añadir luna         |')
        print('| (4) Mostrar planeta     |')
        print('| (5) Modificar planeta   |')
        print('| (6) Eliminar planeta    |')
        print('| (0) Atras               |')
        print('\=========================/')
        opcion = input('->> ')

        if opcion == '1':
            db_handler.imprimir_nombres_documento("moons", {"ref_planet": planeta_obj._id})
        elif opcion == '2':
            get_luna(planeta_obj)
        elif opcion == '3':
            anadir_luna(planeta_obj)
        elif opcion == '4':
            mostrar_planeta(planeta_obj)
        elif opcion == '5':
            modificar_planeta(planeta_obj)
        elif opcion == '6':
            eliminar_planeta(planeta_obj)
        elif opcion == '0':
            break
        else:
            print('\n¡¡¡ Opcion no valida !!!')










# GET LUNA
def get_luna(planeta_obj: Planeta):
    db_handler.imprimir_nombres_documento("moons", {"ref_planet": planeta_obj._id})
    opcion = input('->> ')
    if db_handler.existe_documento("moons", opcion, {"ref_planet": planeta_obj._id}):
        lunas(opcion, planeta_obj)
    else:
        print('\n¡¡¡ Luna no encontrada !!!')

# CREATE LUNA
def anadir_luna(planeta_obj: Planeta):
    data = {"name": input('Nombre->> '),
            "planet":planeta_obj.name,
            "diameter_km": input('Diametro->> '),
            "mass_kg": input('Masa->> '),
            "orbital_period_days": input('Periodo orbital->> '),
            "ref_planet":planeta_obj._id}
    db_handler.anadir_documento("moons", data)
    
# READ LUNA
def mostrar_luna(luna_obj: Luna):
    db_handler.imprimir_documento("moons", luna_obj._id)

# UPDATE LUNA
def modificar_luna(luna_obj: Luna):
    db_handler.modificar_documento("moons", luna_obj._id, {"name": input('Nombre->> '),
            "diameter_km": input('Diametro->> '),
            "mass_kg": input('Masa->> '),
            "orbital_period_days": input('Periodo orbital->> ')})

# DELETE LUNA
def eliminar_luna(luna_obj: Luna):
    db_handler.eliminar_documento("moons", luna_obj._id)

# Menu luna
def lunas(luna_nombre, planeta_obj: Planeta):
    while True:
        luna_data = db_handler.get_documento("moons", luna_nombre)
        luna_obj = Luna(
            str(luna_data['_id']), 
            luna_data['name'], 
            luna_data['ref_planet']
        )

        print('\nLUNA: ' + luna_obj.name)
        print('/=========================\\')
        print('| (1) Mostrar luna        |')
        print('| (2) Modificar luna      |')
        print('| (3) Eliminar luna       |')
        print('| (0) Atras               |')
        print('\=========================/')

        opcion = input('->> ')

        if opcion == '1':
            mostrar_luna(luna_obj)
        elif opcion == '2':
            modificar_luna(luna_obj)
        elif opcion == '3':
            eliminar_luna(luna_obj)
        elif opcion == '0':
            break
        else:
            print('\n¡¡¡ Opcion no valida !!!')





main_menu()