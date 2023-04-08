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

# Sobre o banco de dados:

<p>O banco de dados foi construído com o PostgreSQL, ele será local, não via Docker. Os comando necessários para a criação das tabelas está na pasta BD do projeto, assim como o diagrama do banco de dados.</p>
<p>Atente-se as configurações de usuário, senha e nome do banco de dados. Você pode mudar estes parâmetros no arquivo "carregando.py" na função "conectar".</p>

# Sobre o uso de memória:

<p>O Airflow é uma aplicação pesada, então é importante que tenha 4GB ou mais de memória RAM livre. Pois será inicializado de 6 até 7 serviços diferentes dentro do docker-compose. Então, garanta de ter o suficiente não somente para o Airflow, mas também para o processamento dos dados.</p>