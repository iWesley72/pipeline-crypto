# Pipeline de dados ETL Criptomoedas

<p>Projeto de criação de uma pipeline de dados ETL, utilizando uma API pública, Python e Airflow(via Docker) para obtenção e tratamento dos dados, e banco de dados PostgreSQL para persistir os dados localmente.</p>

## Sobre a API:

<p>Foi utlizada a API de Dados do Mercado Bitcoin, que é livre e não precisa de cadastro para uso.</p>
<p>Documentação: <a href="https://api.mercadobitcoin.net/api/v4/docs">API de Dados V4</a></p>

## Inicializando o Airflow

<p>Para iniciliazar o Airflow é necessário o docker-compose(> 1.29.1), além de ter 4GB ou mais de RAM.</p>
<p>Para configurar o Airflow antes: </p>
<ul>
    <li>Executar no terminal: echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env</li>
    <li>Executar: docker-compose up airflow-init</li>
</ul>
<p>Com isso já temos o Airflow configurado, com usuário e senha padrão sendo "airflow".</p>
<p>Para inicializar o Airflow utilize: docker-compose up. Caso deseje rodar o container em background use a flag -d.</p>
