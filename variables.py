from pymongo import MongoClient
import xmlrpc.client as client


uid = 2
url = "http:// #URL do local host da aplicação "
db = ''
username = ''
password = ''
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))


def crm_execute(model, method, *args):
    return models.execute_kw(db, uid, password, model, method, *args)


class Variables:
    def __init__(self):
        self.mongo_aliest = MongoClient('mongodb:/#caminho para o banco de dados mongoDB/')
        self.crm_aliest = crm_execute
        self.cnpja_auth = {'Authorization': '#código de autorização'}
