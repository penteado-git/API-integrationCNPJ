from requests import get


headers = {
    'Authorization': #código de autorização da API
}

cnpj = #declarar a váriavel CNPJ


def is_cnpj_valido(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))

    if len(cnpj) != 14:
        return False

    if len(set(cnpj)) == 1:
        return False

    def calcular_digito(cnpj, posicao):
        total = 0
        for i, digito in enumerate(cnpj):
            total += int(digito) * posicao[i]
        resto = total % 11
        return str(0 if resto < 2 else 11 - resto)

    posicao1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    posicao2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    digito1 = calcular_digito(cnpj[:12], posicao1)
    digito2 = calcular_digito(cnpj[:12] + digito1, posicao2)

    return cnpj[-2:] == digito1 + digito2


def consultar_cnpj(cnpj):
    url = f"https://api.cnpja.com/office/{cnpj}?simples=true&strategy=CACHE"
    resp = get(url, headers=headers)

    if resp.status_code == 400:
        print("Erro 400: Parâmetro de consulta mal formatado ou faltante")
        return False
    elif resp.status_code == 404:
        print("Erro 404: CNPJ Não registrado na base")
    elif resp.status_code == 401:
        print("Erro 401: Chave de API incorreta")
    elif resp.status_code == 429:
        print("Erro 429: Crédito insuficiente/limite de tempo excedido")
    elif resp.status_code == 529:
        print("Erro Critico 529: Serviço temporariamente ausente")
    elif resp.status_code == 200:
        print("Erro 200: Sucesso na requisição")

        data = resp.json()
        mei = data['company']['simei']['optant']
        situacao = data['status']['text']

        format_rest = {
            "status": True,
            "mei": mei,
            "status_ativo": situacao,
            "cnpj": data['taxId'],
        }

        if mei:
            print("MEI: Sim")
        else:
            print("PJ: Sim")

        print(format_rest)


# Verifica se o CNPJ é válido
if is_cnpj_valido(cnpj):
    consultar_cnpj(cnpj)
else:
    print("CNPJ inválido")
