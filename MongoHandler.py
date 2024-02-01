from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

class MongoHandler:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['universo_db']

    def imprimir_nombres_documento(self, coleccion):
        result = self.db[coleccion].find()

        if result == None:
            print('\nNo se han encontrado resultados')
        else:
            print('\nRESULTADOS:')
            for x in result:
                print('\t' + x['name'])

    def existe_documento(self, coleccion, name):
        result = self.db[coleccion].find_one({"name": name})
        if result == None:
            print('\n¡¡¡ Opcion no valida !!!')
            return False
        else:
            return True

    def imprimir_documento(self, coleccion, name):
        result = self.db[coleccion].find_one({"name": name})

        if result == None:
            print('No se han encontrado resultados')
        else:
            print('\nRESULTADO:')
            pprint('\t' + result)

    def anadir_documento(self, coleccion, data):
        self.db[coleccion].insert_one(data)

    def get_documento(self, coleccion, name):
        return self.db[coleccion].find_one({"name": name})
    