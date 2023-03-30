"""
Tratamento dos dados dos arquivos cotacao.csv e trades.csv

Como os dados já vem quase que completamente tratado pela API, basta transformar as colunas 'date' de cada arquivo. Os dados da coluna 'date' estão no formato Era Unix, mas é fácil mudar o formato, o pandas reconhece o formato e retorna na forma '%Y-%m-%d %H:%M:%S'.

Após isso geraremos um novo arquivo com o os dados tratados.
"""

import pandas as pd
import numpy as np
from extraindo import existeArquivo

def corrigeHora(nomeArquivo:str):
    """
    Função que converte as datas em formato Era Unix para a forma %Y-%m-%d %H:%M:%S'.
    """

    df = pd.read_csv(f'{nomeArquivo}.csv', sep=';')
    df['date'] = pd.to_datetime(df['date'], unit='s')
    
    existeArquivo(nomeArquivo)
    df.to_csv(f'{nomeArquivo}-tratado.csv', sep=';', index=False)
    return df

corrigeHora('cotacao')