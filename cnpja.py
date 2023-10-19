"""
---- CONSULTAS CNPJÁ ----
"""
# %%
from variables import Variables
from requests import get, post
from datetime import datetime


variables = Variables()

class ConsultasCnpj:
    def __init__(self):
        self.cnpja_auth = variables.cnpja_auth


    def classifica_lead(self, cnpj, strategy):
        string_consulta = f"https://api.cnpja.com/office/{cnpj}?simples=true&strategy={strategy}"
        res = get(string_consulta, headers=self.cnpja_auth)

        if res.status_code == 200:
            res = res.json()
            format_res = {
                "status": True,
                "mei": res['company']['simei']['optant'],
                "status_ativo": res['status']['id'],
                "cnpj": cnpj,
                "complete_info": res
            }
            if format_res['mei']:
                format_res['lead_class'] = "mei"

            elif format_res['status_ativo'] != 2:
                format_res['lead_class'] = "inativo"
            
            else:
                format_res['lead_class'] = 'pjtao'
        
        elif res.status_code in [400, 404]:
            format_res = {
                'status': True,
                'lead_class': 'pjta'
            }
        else: 
            format_res = {
                'status': False,
                'lead_class': 'undefined'
            }
        
        return format_res

