from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

uri = "mongodb+srv://admin:admin@universbd.dxuaa8n.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['universo_db']

def print_nombres_documento(coleccion):
    result = db[coleccion].find()

    
    if result == None:
        print('\nNo se han encontrado resultados')
    else:
        print('\nRESULTADOS:')
        for x in result:
            print('\t' + x['name'])


def existeDocumento(coleccion, name):
    result = db[coleccion].find_one({"name": name})
    if result == None:
        print('\n¡¡¡ Opcion no valida !!!')
        return False
    else:
        return True


def print_documento(coleccion, name):
    result = db[coleccion].find_one({"name": name})

    
    if result == None:
        print('No se han encontrado resultados')
    else:
        print('\nRESULTADO:')
        pprint('\t' + result)


# # # # # # # # # # # # # # #
# |--galaxias               #
#   |-- sistemas solares    #
#     |-- estrellas         #
#     |-- planetas          #
#       |-- lunas           #
# # # # # # # # # # # # # # #


# |--galaxias
def get_galaxia():
    print_nombres_documento("galaxies")
    opcion = input('->> ')
    if existeDocumento("glaxies", opcion):    
        galaxia(opcion)
    else:
        mainMenu()

def galaxia():
    print('\nGALAXIA: ' + galaxia)
    print('/=========================\\')
    print('| (1) Mostrar sistemas    |')
    print('| (2) Seleccionar sistema |')
    print('| (3) Añadir sistema      |')
    print('| (4) Mostrar galaxia     |')
    print('| (5) Modificar galaxia   |')
    print('| (0) Atras               |')
    print('\=========================/')
    opcion = input('->> ')
    if opcion == '1':
        print_nombres_documento("galaxies")
    elif opcion == '2':
        galaxia()
    elif opcion == '3':
        print('añadir galaxia')
    elif opcion == '0':
        exit()
    else:
        print('\n¡¡¡ Opcion no valida !!!')
        

# |--galaxia
#   |-- sistemas solares


# |--galaxia
#   |-- sistema solar
#     |-- estrellas


# |--galaxia
#   |-- sistema solar
#     |-- planetas


# |--galaxia
#   |-- sistema solar
#     |-- planeta
#       |-- lunas


def mainMenu():
    # MAIN MENU
    print('\n/=========================\\')
    print('| (1) Mostrar galaxias    |')
    print('| (2) Seleccionar galaxia |')
    print('| (3) Añadir galaxia      |')
    print('| (0) Salir               |')
    print('\=========================/')
    opcion = input('->> ')
    if opcion == '1':
        print_nombres_documento("galaxies")
    elif opcion == '2':
        get_galaxia()
    elif opcion == '3':
        print('añadir galaxia')
    elif opcion == '0':
        exit()
    else:
        print('\n¡¡¡ Opcion no valida !!!')
        mainMenu()


mainMenu()