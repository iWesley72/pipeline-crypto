import requests

def simbolos() -> list:
    """
    Função para obter os ativos disponíveis no Mercado Bitcoin que sejam criptomoedas, a partir de sua API de Dados.
    """

    simb = requests.get('https://api.mercadobitcoin.net/api/v4/symbols').json()
    simb = [simb.get('base-currency'), simb.get('description'), simb.get('type')]

    criptos = [[], []]
    for i in range(0, len(simb[2])):
        match simb[2][i]:
            case 'CRYPTO':
                criptos[0].append(simb[0][i])
                criptos[1].append(simb[1][i])
            case other:
                pass
    


    return criptos

def cotacao() -> list:
    """
    Função para extrair o resumo das últimas 24 horas de negociação.
    """
    
    ativos = simbolos()
    cotacao = list()
    for ativo in ativos[0]:
        dado = requests.get(f'https://api.mercadobitcoin.net/api/v4/tickers/?symbols={ativo}-BRL').json()
        cotacao.append(dado)

    return cotacao

def extrair(dataInicio=None, dataFim=None) -> list:
    """
    Função para extrair os dados da API de Dados do Mecado Bitcoin de um intervalo de tempo, ou das últimas 1000 negociações caso não seja informado período.

    Argumentos opcionais:
    dataInicio: data inicial do período desejado (obrigatóriamente em Era Unix), caso seja informado dataInicio, deverá também ser informado dataFim.
    dataFim: data final do período desejado (obrigatóriamente em Era Unix), caso seja informado dataFim, deverá também ser informado dataInicio.
    """
    
    dados = list()
    ativos = simbolos()
    for ativo in ativos[0]:
        try:
            req = requests.get(f'https://api.mercadobitcoin.net/api/v4/{ativo}-BRL/trades/?from={dataInicio}/?to={dataFim}').json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        dados.append(req)
    return dados

print(cotacao())