from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import extraindo
# import carregando
import transformando

with DAG("etl",
         start_date=datetime(2023, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:
    
    # Extraindo dados:
    extraindo_simbolos_trades = PythonOperator(
        task_id="extraindo_simbolos_trades",
        python_callable=extraindo.extrair
    )

    extraindo_cotacao = PythonOperator(
        task_id="extraindo_cotacao",
        python_callable=extraindo.cotacao
    )

    # Transformando dados:

    transformando_trades = PythonOperator(
        task_id="transformando_trades",
        python_callable=transformando.transformar,
        op_kwargs={'nomeArquivo':'trades'}
    )

    transformando_cotacao = PythonOperator(
        task_id="transformando_cotacao",
        python_callable=transformando.transformar,
        op_kwargs={'nomeArquivo':'cotacao'}
    )

extraindo_simbolos_trades >> extraindo_cotacao >> transformando_trades >> transformando_cotacao
