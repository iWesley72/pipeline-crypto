import pandas as pd
import numpy as np
import psycopg2

def conectar():
    try:
        """
        Função responsável por fazer a conexão com o banco de dados e retornar o cursor, para que seja possível trabalhar o banco de dados.
        """

        conn = psycopg2.connect(
            user='postgres',
            password='admin123',
            host='host.docker.internal',
            port='5432',
            database='cripto'
        )
    except (Exception, psycopg2.Error) as err:
        print('Erro ao conectar no banco de dados\n', err)
    print('Conexão bem sucedida')
    return conn

def atualizarTabela(tabela:str):
    conn = conectar()
    if tabela == 'cripto':
        columns = pd.read_csv(f'{tabela}.csv', sep=';').columns.values.tolist()
    else:
        columns = pd.read_csv(f'{tabela}-tratado.csv', sep=';').columns.values.tolist()
    cursor = conn.cursor()
    try:
        if tabela == 'cripto':
            with open(f'{tabela}.csv') as csvFile:
                next(csvFile)
                cursor.copy_from(csvFile, tabela, sep=';', null='', columns=columns)
                conn.commit()
        else:
            with open(f'{tabela}-tratado.csv') as csvFile:
                next(csvFile)
                cursor.copy_from(csvFile, tabela, sep=';', null='', columns=columns)
                conn.commit()
    except (Exception, psycopg2.Error) as err:
        print('Erro ao atualizar tabela\n', err)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()
    conn.close()
