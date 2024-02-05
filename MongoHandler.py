from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

class MongoHandler:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['universo_db']

    def imprimir_nombres_documento(self, coleccion, filtro = {}):
        if filtro == {}:
            result = self.db[coleccion].find()
        else: 
            result = self.db[coleccion].find(filtro)
            
        if result == None:
            print('\nNo se han encontrado resultados')
        else:
            print('\nRESULTADOS:')
            for x in result:
                print('\t' + x['name'])

    def imprimir_documento(self, coleccion, _id):
        result = self.db[coleccion].find_one({"_id": _id})

        if result == None:
            print('No se han encontrado resultados')
        else:
            print('\nRESULTADO:')
            pprint(result)

    def get_documento(self, coleccion, name):
        return self.db[coleccion].find_one({"name": name})

    def existe_documento(self, coleccion, name, filtro = {}):
        if filtro == {}:
            result = self.db[coleccion].find_one({"name": name})
        else:
            result = self.db[coleccion].find_one({filtro})
            
        if result == None:
            print('\n¡¡¡ Opcion no valida !!!')
            return False
        else:
            return True

    def anadir_documento(self, coleccion, data):
        self.db[coleccion].insert_one(data)

    def modificar_documento(self, coleccion, _id, data):
        self.db[coleccion].update_one({"_id": _id}, {"$set": data})

    def eliminar_documento(self, coleccion, _id):
        self.db[coleccion].delete_one({"_id": _id})

    