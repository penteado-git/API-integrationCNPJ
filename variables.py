from pymongo import MongoClient
import xmlrpc.client as client


uid = 2
url = "http://192.168.196.125:8070/"
db = 'odoo2'
username = 'Administrator'
password = 'Solere1122!@'
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))


def crm_execute(model, method, *args):
    return models.execute_kw(db, uid, password, model, method, *args)


class Variables:
    def __init__(self):
        self.mongo_aliest = MongoClient('mongodb://ali2:Teste%402020@192.168.196.101:27017/?authMechanism=DEFAULT')
        self.crm_aliest = crm_execute
        self.cnpja_auth = {'Authorization': '3e7fa31b-2e5c-4ca5-b0c6-26a8f1745d68-fbd473bc-efea-4249-8d5f-06da38d1025d'}
