CREATE TABLE cripto(
	id_cripto VARCHAR(10),
	descricao VARCHAR(20),
	PRIMARY KEY(id_cripto)
);

CREATE TABLE trades(
	id_trade SERIAL,
	"date" TIMESTAMP,
	"type" VARCHAR(4),
	price FLOAT(8),
	amount FLOAT(8),
	id_cripto VARCHAR(10),
	PRIMARY KEY(id_trade),
	CONSTRAINT fk_cripto FOREIGN KEY(id_cripto) REFERENCES cripto(id_cripto)
);

CREATE TABLE cotacao(
	id_cotacao SERIAL,
	pair VARCHAR(10),
	high FLOAT(8),
	low FLOAT(8),
	vol FLOAT(8),
	"last" FLOAT(8),
	buy FLOAT(8),
	sell FLOAT(8),
	"open" FLOAT(8),
	"date" TIMESTAMP,
	id_cripto VARCHAR(10),
	PRIMARY KEY(id_cotacao),
	CONSTRAINT fk_cripto FOREIGN KEY(id_cripto) REFERENCES cripto(id_cripto)
);