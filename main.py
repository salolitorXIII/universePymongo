from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint


def cargar_datos(coleccion):
    uri = "mongodb+srv://admin:admin@universbd.dxuaa8n.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client['universo_db']
    result = db[coleccion].find()

    
    if result == None:
        print('No se han encontrado resultados')
    else:
        print('\nRESULTADOS:')
        for x in result:
            print('\t' + x['name'])


# # # # # # # # # # # # # # #
# |--galaxias               #
#   |-- sistemas solares    #
#     |-- estrellas         #
#     |-- planetas          #
#       |-- lunas           #
# # # # # # # # # # # # # # #

# |--galaxias               
def mostrar_galaxias():
    cargar_datos("galaxies")


def selecionar_galaxia():
    mostrar_galaxias()
    galaxia = input('->> ')

    print('\nGALAXIA: ' + galaxia)
    print('/=========================\\')
    print('|  (1) Mostrar sistemas   |')
    print('| (2) Seleccionar sistema |')
    print('|   (3) Añadir sistema    |')
    print('|  (4) Modificar galaxia  |')
    print('|       (0) Atras         |')
    print('\=========================/')
    opcion = input('->> ')


# |--galaxia
#   |-- sistemas solares
def mostrar_sistemas_solares():
    cargar_datos("solar_systems")


# |--galaxia
#   |-- sistema solar
#     |-- estrellas
def mostrar_estrellas():
    cargar_datos("stars")


# |--galaxia               
#   |-- sistema solar         
#     |-- planetas          
def mostrar_planetas():
    cargar_datos("planets")


# |--galaxia               
#   |-- sistema solar   
#     |-- planeta          
#       |-- lunas           
def mostrar_lunas():
    cargar_datos("moons")


def mainMenu():
    # MAIN MENU
    print('\n/=========================\\')
    print('|  (1) Mostrar galaxias   |')
    print('| (2) Seleccionar galaxia |')
    print('|   (3) Añadir galaxia    |')
    print('|       (0) Salir         |')
    print('\=========================/')
    opcion = input('->> ')
    if opcion == '1':
        mostrar_galaxias()
    if opcion == '2':
        selecionar_galaxia()
    if opcion == '3':
        print('añadir galaxia')
    if opcion == '0':
        exit()
    else:
        print('\n¡¡¡ Opcion no valida !!!')
        mainMenu()


mainMenu()